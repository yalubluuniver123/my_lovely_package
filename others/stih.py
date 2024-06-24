import random

from PIL import Image, ImageDraw


# def get_color(char, char_type):
#     if char_type == "vowel":
#         vowels = "ауоиэеёюяыьъ"
#         colors = [(255, 255, 0), (255, 165, 0), (255, 0, 0)]
#         return colors[vowels.index(char) % len(colors)]
#     elif char_type == "consonant":
#         consonants = "бвгджзйклмнпрстфхцчшщ"
#         colors = [(0, 255, 0), (0, 255, 255), (0, 0, 255), (128, 0, 128)]
#         return colors[consonants.index(char) % len(colors)]
#     else:
#         return 128, 128, 128

# Функция для получения оттенка цвета в зависимости от символа
def get_color(char):
    vowels = "АУОИЭЕЁЮЯЫЬЪ"
    consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    punctuation = ".!?,;:()[]{}\"'"

    if char.isalpha():
        if char.upper() in vowels:
            vowel_colors = [(255, 255, 0), (255, 165, 0), (255, 0, 0)]
            vowel_index = vowels.index(char.upper())
            return vowel_colors[vowel_index % len(vowel_colors)]
        else:
            consonant_colors = [(0, 255, 0), (0, 255, 255), (0, 0, 255), (128, 0, 128)]
            consonant_index = consonants.index(char.upper())
            return consonant_colors[consonant_index % len(consonant_colors)]
    elif char in punctuation:
        punctuation_colors = [(128, 128, 128), (150, 150, 150), (170, 170, 170), (190, 190, 190), (210, 210, 210),
                              (230, 230, 230)]
        punctuation_index = punctuation.index(char)
        return punctuation_colors[punctuation_index % len(punctuation_colors)]
    else:
        return 255


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
            color = get_color(char.lower()) + (random.randint(0, 255))
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
            color = get_color(char) + (random.randint(25, 255))
            draw.rectangle([x, y, x + square_size, y + square_size], fill=color)
            x += square_size
            if x + square_size > image_width:
                x = 0
                y += square_size

    x = 0
    y += square_size

image_resolution = 300
image.save("text_image.png", dpi=(image_resolution, image_resolution))
