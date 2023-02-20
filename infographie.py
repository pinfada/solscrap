from PIL import Image, ImageDraw, ImageFont

# Dimensions de l'image
IMAGE_WIDTH = 1000
IMAGE_HEIGHT = 800

# Dimensions de l'image centrale
CENTER_IMAGE_WIDTH = 500
CENTER_IMAGE_HEIGHT = 500

# Position de l'image centrale
CENTER_IMAGE_X = IMAGE_WIDTH // 2 - CENTER_IMAGE_WIDTH // 2
CENTER_IMAGE_Y = IMAGE_HEIGHT // 2 - CENTER_IMAGE_HEIGHT // 2

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
product_image = product_image.resize((CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT))

# Création de l'image centrale
center_image = Image.new('RGB', (CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT), (255, 255, 255))
center_image.paste(product_image, (0, 0))
center_image_draw = ImageDraw.Draw(center_image)
center_image_font = ImageFont.truetype('DejaVuSansMono.ttf', 40)
center_image_draw.text((CENTER_IMAGE_WIDTH // 2, CENTER_IMAGE_HEIGHT + 20), product_name, fill=(0, 0, 0), font=center_image_font, anchor='ms')

# Création des étapes de cuisson
cooking_steps_image = Image.new('RGB', (400, 400), (255, 255, 255))
cooking_steps_draw = ImageDraw.Draw(cooking_steps_image)
cooking_steps_font = ImageFont.truetype('DejaVuSansMono.ttf', 20)
step_y = 50
for step in cooking_steps:
    cooking_steps_draw.text((50, step_y), step, fill=(0, 0, 0), font=cooking_steps_font, anchor='lm')
    step_y += 30

# Création des avantages pour la santé
health_benefits_image = Image.new('RGB', (400, 400), (255, 255, 255))
health_benefits_draw = ImageDraw.Draw(health_benefits_image)
health_benefits_font = ImageFont.truetype("DejaVuSansMono.ttf", 20)
benefit_y = 50
for benefit, description in health_benefits.items():
    health_benefits_draw.text((50, benefit_y), "• " + benefit, fill=(0, 0, 0), font=health_benefits_font, anchor="lt")
    health_benefits_draw.text((250, benefit_y), description, fill=(0, 0, 0), font=health_benefits_font, anchor="rt")
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