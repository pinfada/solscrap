from PIL import Image, ImageDraw, ImageFont
import textwrap

def adjust_text_size(text, font, max_width, font_file):
    # Calcule la taille actuelle du texte
    current_width, current_height = font.getsize(text)

    # Si la taille actuelle est inférieure à la taille maximale, retourne simplement la police actuelle
    if current_width <= max_width:
        return font

    # Trouve la taille de police maximale qui convient
    max_font_size = get_max_font_size(text, max_width, font_file)

    # Crée la police à partir de la taille maximale trouvée
    font = ImageFont.truetype(font_file, max_font_size)

    # Effectue un retour à la ligne automatique si nécessaire
    text = wordWrap(text, max_width)

    return font, text


# Ce code permet de Redimensionner et recadrer une image à la taille spécifiée tout en maintenant les proportions d'origine
def resize_and_crop_image(image, size):
    ratio = image.width / image.height
    new_size = (int(min(size[1]*ratio, size[0])), int(min(size[0]/ratio, size[1])))
    image = image.resize(new_size)
    width, height = image.size
    left = (width - size[0]) // 2
    top = (height - size[1]) // 2
    right = left + size[0]
    bottom = top + size[1]
    image = image.crop((left, top, min(right, width), min(bottom, height)))
    return image

def get_max_font_size(text, max_width, font_file):
    font_size = 1
    while True:
        font = ImageFont.truetype(font_file, font_size)
        width, height = font.getsize(text)
        if width > max_width:
            return font_size - 1
        font_size += 1

def wordWrap(text, max_width, line_spacing=1.0):
    lines = textwrap.wrap(text, width=max_width)
    spacer_add = min(len(lines) * line_spacing, 0.5) * max_width
    return spacer_add, "\n".join(lines)


# Dimensions de l'image
IMAGE_WIDTH = 2000
IMAGE_HEIGHT = 1600

# Dimensions de l'image centrale
CENTER_IMAGE_WIDTH = 250
CENTER_IMAGE_HEIGHT = 250

# Position de l'image centrale
CENTER_IMAGE_X = IMAGE_WIDTH // 2 - CENTER_IMAGE_WIDTH // 2
CENTER_IMAGE_Y = IMAGE_HEIGHT // 2 - CENTER_IMAGE_HEIGHT // 2

# typologie texte
font_file = "DejaVuSansMono.ttf"
max_width = 150

palette_couleur = {'fonts':
                {'h1': {'font': ImageFont.truetype("DejaVuSansMono.ttf", 40), 'color': (0, 0, 0)},
                 'h2': {'font': ImageFont.truetype("DejaVuSansMono.ttf", 66), 'color': (0, 63, 100)},
                 'h3': {'font': ImageFont.truetype("DejaVuSansMono.ttf", 66), 'color': (172, 213, 230)},
                 'p1': {'font': ImageFont.truetype("DejaVuSansMono.ttf", 30), 'color': (0, 0, 0)},
                 'p2': {'font': ImageFont.truetype("DejaVuSansMono.ttf", 30), 'color': (172, 213, 230)},
                 'p3': {'font': ImageFont.truetype("DejaVuSansMono.ttf", 45), 'color': (172, 213, 230)}},
                'colors': {'bg1': (255, 255, 255), 'bg2': (0, 63, 100), 'logoext': '-dark'}
                }

# Données sur le fruit du dragon
product_name = 'Fruit du dragon'
cooking_steps = [
    '1. Laver et couper le fruit en deux.',
    '2. Retirer la peau et couper la chair en morceaux.',
    '3. Ajouter du sucre et de l\'eau.',
    '4. Faire cuire pendant 30 minutes à feu moyen.',
    '5. Laisser refroidir et servir.'
]
health_benefits = {
    'Source de potassium': 'Contribue à une fonction musculaire normale.',
    'Source de vitamine C': 'Favorise le système immunitaire.',
    'Faible en calories': 'Peut aider à la gestion du poids.',
    'Source de fibres': 'Favorise la digestion.',
    'Riche en antioxydants': 'Peut aider à réduire l\'inflammation.'
}
fun_facts = [
    'Le fruit du dragon est également connu sous le nom de pitahaya.',
    'Il est originaire d\'Amérique centrale et d\'Amérique du Sud.',
    'Le fruit est souvent utilisé en cuisine asiatique pour ajouter de la couleur et de la saveur.'
]

# Chargement de l'image du fruit du dragon
product_image = Image.open('images/fruit_dragon.jpg')

product_image = resize_and_crop_image(product_image, (CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT))

# Création de l'image centrale
# center_image = Image.new('RGB', (CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT), (255, 255, 255))
center_image = Image.new('RGB', (CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT), palette_couleur['colors']['bg1'])
center_image.paste(product_image, (0, 0))
center_image_draw = ImageDraw.Draw(center_image)
center_image_font = ImageFont.truetype('DejaVuSansMono.ttf', 40)
center_image_draw.text((CENTER_IMAGE_WIDTH // 2, CENTER_IMAGE_HEIGHT + 20), product_name, fill=(0, 0, 0), font=center_image_font, anchor='ms')

# Création des étapes de cuisson
cooking_steps_image = Image.new('RGB', (400, 400), palette_couleur['colors']['bg1'])
cooking_steps_draw = ImageDraw.Draw(cooking_steps_image)
#cooking_steps_font = ImageFont.truetype('DejaVuSansMono.ttf', 20)
step_y = 50
for step in cooking_steps:
    font_size = get_max_font_size(step, max_width, font_file)
    #print("cooking font size : ", font_size)
    #print("cooking step phrase : ", step)
    font = ImageFont.truetype(font_file, font_size)
    cooking_steps_font = adjust_text_size(step, font, max_width, font_file)
    cooking_steps_draw.text((10, step_y), step, fill=(0, 0, 0), font=cooking_steps_font, anchor='lm')
    step_y += 30

# Création des avantages pour la santé
health_benefits_image = Image.new('RGB', (400, 400), palette_couleur['colors']['bg1'])
health_benefits_draw = ImageDraw.Draw(health_benefits_image)

benefit_y = 50
for benefit, description in health_benefits.items():
    #health_benefits_font = adjust_text_size(benefit, ImageFont.truetype("DejaVuSansMono.ttf", 20), 200)
    font_size = get_max_font_size(benefit, max_width, font_file)
    font = ImageFont.truetype(font_file, font_size)
    health_benefits_font = adjust_text_size(benefit, font, max_width, font_file)
    health_benefits_draw.text((30, benefit_y), "• " + benefit, fill=(0, 0, 0), font=health_benefits_font, anchor="lt")
    
    #health_benefits_font = adjust_text_size(description, ImageFont.truetype("DejaVuSansMono.ttf", 20), 200)
    health_benefits_font = adjust_text_size(benefit, font, max_width, font_file)
    health_benefits_draw.text((200, benefit_y), description, fill=(0, 0, 0), font=health_benefits_font, anchor="lt")
    benefit_y += 50

# Création de l'image d'anecdotes
anecdotes_image = Image.new('RGB', (800, 100), (255, 255, 255))
anecdotes_draw = ImageDraw.Draw(anecdotes_image)
anecdotes_font = ImageFont.truetype('DejaVuSansMono.ttf', 16)
anecdotes_draw.text((400, 50), "Anecdotes sur le fruit du dragon", fill=(0, 0, 0), font=anecdotes_font, anchor='mm')

# Assemblage des différentes parties de l'infographie
final_image = Image.new('RGB', (800, 800), (255, 255, 255))
final_image.paste(product_image, (200, 100))
final_image.paste(cooking_steps_image, (600, 100))
final_image.paste(health_benefits_image, (200, 500))
final_image.paste(anecdotes_image, (400, 700))

# Enregistrement de l'image finale
final_image.save('fruit_du_dragon.png')
