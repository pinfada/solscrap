from PIL import Image, ImageDraw, ImageFont
import textwrap

def get_max_font_size(text, max_width, font_file):
    """Trouve la taille maximale de police pour le texte donné."""
    font_size = 1
    font = ImageFont.truetype(font_file, font_size)
    while font.getlength(text) < max_width:
        font_size += 1
        font = ImageFont.truetype(font_file, font_size)
    return font_size - 1


def adjust_text_size(text, font, max_width, font_file):
    """Ajuste la taille de police pour s'adapter à la largeur maximale."""
    text_width = font.getlength(text)

    # Vérifie si le texte doit être redimensionné
    if text_width <= max_width:
        return font, text

    # Trouve la taille de police maximale pour le texte
    max_font_size = get_max_font_size(text, max_width, font_file)

    # Crée la police à partir de la taille maximale trouvée
    font = ImageFont.truetype(font_file, max_font_size)

    # Effectue un retour à la ligne automatique si nécessaire
    text = word_wrap(text, max_width, font)

    return font, text


def word_wrap(text, max_width, font):
    """Effectue un retour à la ligne automatique pour le texte donné."""
    words = text.split()
    lines = []
    current_line = words[0]
    for word in words[1:]:
        if font.getsize(current_line + ' ' + word)[0] <= max_width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return '\n'.join(lines)

# Ce code permet de Redimensionner et recadrer une image à la taille spécifiée tout en maintenant les proportions d'origine
from PIL import Image

def resize_and_crop_image(image, size, crop_position='center'):
    # Vérification des arguments
    if not isinstance(image, Image.Image):
        raise ValueError("L'argument 'image' doit être un objet Image.")
    if not isinstance(size, tuple) or len(size) != 2 or not all(isinstance(dim, int) for dim in size):
        raise ValueError("L'argument 'size' doit être un tuple de deux entiers.")
    if crop_position not in ['center', 'top-left', 'top-right', 'bottom-left', 'bottom-right']:
        raise ValueError("L'argument 'crop_position' doit être 'center', 'top-left', 'top-right', 'bottom-left' ou 'bottom-right'.")

    # Calcul du ratio
    if image.height == 0:
        raise ValueError("La hauteur de l'image est nulle.")
    ratio = image.width / image.height
    
    # Calcul de la nouvelle taille en respectant le ratio
    new_ratio = size[0] / size[1]
    if ratio > new_ratio:
        new_size = (int(size[1] * ratio), size[1])
    else:
        new_size = (size[0], int(size[0] / ratio))

    # Redimensionnement de l'image
    resized_image = image.copy().resize(new_size)

    # Recadrage de l'image
    x_start, y_start = 0, 0
    x_end, y_end = size[0], size[1]
    if crop_position == 'center':
        x_start = (new_size[0] - size[0]) // 2
        y_start = (new_size[1] - size[1]) // 2
        x_end = x_start + size[0]
        y_end = y_start + size[1]
    elif crop_position == 'top-left':
        x_end = min(new_size[0], size[0])
        y_end = min(new_size[1], size[1])
    elif crop_position == 'top-right':
        x_start = max(0, new_size[0] - size[0])
        x_end = new_size[0]
        y_end = min(new_size[1], size[1])
    elif crop_position == 'bottom-left':
        x_end = min(new_size[0], size[0])
        y_start = max(0, new_size[1] - size[1])
        y_end = new_size[1]
    elif crop_position == 'bottom-right':
        x_start = max(0, new_size[0] - size[0])
        x_end = new_size[0]
        y_start = max(0, new_size[1] - size[1])
        y_end = new_size[1]
    cropped_image = resized_image.crop((x_start, y_start, x_end, y_end))

    return cropped_image

# Dimensions de l'image centrale
CENTER_IMAGE_WIDTH = 250
CENTER_IMAGE_HEIGHT = 250

# typologie texte
font_file = "DejaVuSansMono.ttf"
max_width = 300

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
logo_titre = "Tchopmygrinds"
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

# Chargement du logo de l'entreprise
logo_image = Image.open('images/logo-tchopmygrinds.png')
logo_update = resize_and_crop_image(logo_image, (100, 100))
company_image = Image.new('RGB', (100, 100), palette_couleur['colors']['bg1'])
company_image_draw = ImageDraw.Draw(company_image)
company_image_font = ImageFont.truetype('DejaVuSansMono.ttf', 15)
company_image_draw.text((45, 10), logo_titre, fill=palette_couleur['fonts']['h1']['color'], font=company_image_font, anchor='ms')

# Chargement de l'image du fruit du dragon
product_image = Image.open('images/fruit_dragon.jpg')
product_image = resize_and_crop_image(product_image, (CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT))
center_image = Image.new('RGB', (CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT), palette_couleur['colors']['bg1'])
center_image.paste(product_image, (0, 0))
center_image_draw = ImageDraw.Draw(center_image)
center_image_font = ImageFont.truetype('DejaVuSansMono.ttf', 40)
center_image_draw.text((CENTER_IMAGE_WIDTH // 2, CENTER_IMAGE_HEIGHT + 20), product_name, fill=palette_couleur['fonts']['h1']['color'], font=center_image_font, anchor='ms')

# Création des étapes de cuisson
cooking_steps_image = Image.new('RGB', (400, 200), palette_couleur['colors']['bg1'])
cooking_steps_draw = ImageDraw.Draw(cooking_steps_image)
step_y = 50
for step in cooking_steps:
    font_size = get_max_font_size(step, max_width, font_file)
    font = ImageFont.truetype(font_file, font_size)
    cooking_steps_font, cooking_text = adjust_text_size(step, font, max_width, font_file)
    cooking_steps_draw.text((30, step_y), step, fill=palette_couleur['fonts']['h2']['color'], font=cooking_steps_font, anchor='lm')
    step_y += 30

# Création des avantages pour la santé
health_benefits_image = Image.new('RGB', (750, 300), palette_couleur['colors']['bg1'])
health_benefits_draw = ImageDraw.Draw(health_benefits_image)

benefit_y1 = benefit_y2 = 50
for benefit, description in health_benefits.items():
    #health_benefits_font = adjust_text_size(benefit, ImageFont.truetype("DejaVuSansMono.ttf", 20), 200)
    font_size = get_max_font_size(benefit, max_width, font_file)
    font = ImageFont.truetype(font_file, font_size)
    health_benefits_font, benefit_text = adjust_text_size(benefit, font, max_width, font_file)
    text_width = health_benefits_font.getlength(benefit_text)
    health_benefits_draw.text(((max_width - text_width) / 2, benefit_y1), "• " + benefit_text, fill=palette_couleur['fonts']['h1']['color'], font=health_benefits_font, anchor="lt")
    benefit_y1 += 40

    #health_benefits_font = adjust_text_size(description, ImageFont.truetype("DejaVuSansMono.ttf", 20), 200)
    font_size = get_max_font_size(description, max_width, font_file)
    font = ImageFont.truetype(font_file, font_size)
    health_benefits_font, description_text = adjust_text_size(description, font, max_width, font_file)
    text_width = health_benefits_font.getlength(description_text)
    health_benefits_draw.text((((max_width - text_width) / 2) + 350 , benefit_y2), description_text, fill=palette_couleur['fonts']['h1']['color'], font=health_benefits_font, anchor='lt')
    benefit_y2 += 40

# Création de l'image d'anecdotes
text = "Anecdotes sur le fruit du dragon"
anecdotes_image = Image.new('RGB', (max_width, 100), palette_couleur['colors']['bg1'])
anecdotes_draw = ImageDraw.Draw(anecdotes_image)
font_size = get_max_font_size(text, max_width, font_file)
font = ImageFont.truetype(font_file, font_size)
anecdotes_font, anectdotes_text = adjust_text_size(text, font, max_width, font_file)
text_width = anecdotes_font.getlength(text)
anecdotes_draw.text(((max_width - text_width) / 2, 0), text, fill=palette_couleur['fonts']['h1']['color'], font=anecdotes_font, anchor='lt')


# Création des anecdotes
fun_facts_image = Image.new('RGB', (max_width, 50), palette_couleur['colors']['bg1'])
fun_facts_draw = ImageDraw.Draw(fun_facts_image)
fun_y = 10
for fun in fun_facts:
    font_size = get_max_font_size(fun, max_width, font_file)
    font = ImageFont.truetype(font_file, font_size)
    fun_facts_font, fun_facts_text = adjust_text_size(fun, font, max_width, font_file)
    text_width = fun_facts_font.getlength(fun_facts_text)
    fun_facts_draw.text(((max_width - text_width) / 2, fun_y), fun_facts_text, fill=palette_couleur['fonts']['h1']['color'], font=fun_facts_font, anchor='lm')
    fun_y += 15


# Assemblage des différentes parties de l'infographie
final_image = Image.new('RGB', (800, 800), palette_couleur['colors']['bg2'])
final_image.paste(logo_update, (10, 10))
final_image.paste(product_image, (300, 300))
final_image.paste(cooking_steps_image, (0, 250))
final_image.paste(health_benefits_image, (25, 500))
final_image.paste(anecdotes_image, (300, 100))
final_image.paste(fun_facts_image, (300, 120))

# Enregistrement de l'image finale
final_image.save('fruit_du_dragon.png')
