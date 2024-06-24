import random
from PIL import Image, ImageDraw

def get_color(char):
    vowels = "АУОИЭЕЁЮЯЫЬЪ"
    consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    punctuation = ".!?,;:()[]{}\"'"

    if char.isalpha():
        if char.upper() in vowels:
            vowel_colors = [
    # Оттенки желтого
    (255, 255, 0), (255, 255, 102), (255, 255, 51), (255, 215, 0),
    # Оттенки оранжевого
    (255, 165, 0), (255, 140, 0), (255, 127, 80), (255, 99, 71),
    # Оттенки красного
    (255, 0, 0), (220, 20, 60), (178, 34, 34), (255, 105, 180)
]

            vowel_index = vowels.index(char.upper())
            return vowel_colors[vowel_index % len(vowel_colors)]
        else:
            consonant_colors = [
                # Оттенки зеленого
                (144, 238, 144), (0, 255, 0), (50, 205, 50), (0, 201, 87), (189, 183, 107),
                # Оттенки голубого
                (135, 206, 250), (0, 191, 255), (127, 255, 212), (176, 224, 230), (64, 224, 208),
                # Оттенки синего
                (135, 206, 250), (100, 149, 237), (0, 0, 255), (0, 0, 205), (75, 0, 130),
                (230, 230, 250), (148, 0, 211), (138, 43, 226), (128, 0, 128), (147, 112, 219)
            ]

            consonant_index = consonants.index(char.upper())
            return consonant_colors[consonant_index % len(consonant_colors)]
    elif char in punctuation:
        punctuation_colors = [
            (128, 128, 128),  # Medium Gray
            (140, 140, 140),  # Slightly Lighter Gray
            (152, 152, 152),  # Light Gray
            (164, 164, 164),  # Lighter Gray
            (176, 176, 176),  # Even Lighter Gray
            (188, 188, 188),  # Very Light Gray
            (200, 200, 200),  # Pale Gray
            (212, 212, 212),  # Paler Gray
            (224, 224, 224),  # Very Pale Gray
            (236, 236, 236),  # Extremely Pale Gray
            (248, 248, 248),  # Near White Gray
            (220, 220, 220),  # Light Silver Gray
            (210, 210, 210),  # Silver Gray
            (190, 190, 190)   # Dark Silver Gray
        ]
        punctuation_index = punctuation.index(char)
        return punctuation_colors[punctuation_index % len(punctuation_colors)]
    else:
        return 255, 255, 255

with open("stih.txt", "r") as file:
    lines = file.readlines()

image_width = 3500
image_height = 3000
image = Image.new("RGBA", (image_width, image_height), color="white")
draw = ImageDraw.Draw(image)

square_size = 50

x = 0
y = 0

for text in lines:
    text = text.replace("\n", "")
    for char in text:
        if char.isalpha():
            char_type = "vowel" if char.lower() in "ауоиэеёюяыьъ" else "consonant"
            color = get_color(char.lower()) + (random.randint(0, 255),)
            draw.rectangle([x, y, x + square_size, y + square_size], fill=color)
            x += square_size
            if x + square_size > image_width:
                x = 0
                y += square_size
        elif char == " ":
            x += square_size
            if x + square_size > image_width:
                x = 0
                y += square_size
        else:
            color = get_color(char) + (random.randint(25, 255),)
            draw.rectangle([x, y, x + square_size, y + square_size], fill=color)
            x += square_size
            if x + square_size > image_width:
                x = 0
                y += square_size

    x = 0
    y += square_size

image_resolution = 300
image.save("text_image.png", dpi=(image_resolution, image_resolution))
