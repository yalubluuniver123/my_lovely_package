import matplotlib.pyplot as plt

# Создание прямоугольника
rectangle = plt.Rectangle((0, 0), 1, 1, edgecolor='black', facecolor='none')
plt.gca().add_patch(rectangle)

# Разбиение прямоугольника
num_horizontal = int(input("Введите количество прямоугольников по горизонтали: "))
num_vertical = int(input("Введите количество прямоугольников по вертикали: "))

# Определение цветовой гаммы
colors = ['red', 'green', 'blue', 'yellow', 'orange']

# Определение размеров прямоугольников
rect_width = 1 / num_horizontal
rect_height = 1 / num_vertical

# Определение центрального прямоугольника
center_x = (num_horizontal - 1) / 2 * rect_width
center_y = (num_vertical - 1) / 2 * rect_height

# Определение порядка окрашивания по спирали
spiral_order = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0

# Окраска прямоугольников
color_index = 0
current_x = center_x
current_y = center_y

for i in range(num_horizontal * num_vertical):
    rectangle = plt.Rectangle((current_x, current_y), rect_width, rect_height, edgecolor='black', facecolor=colors[color_index])
    plt.gca().add_patch(rectangle)

    current_x += spiral_order[direction % 4][0] * rect_width
    current_y += spiral_order[direction % 4][1] * rect_height

    direction += 1
    color_index = (color_index + 1) % len(colors)

plt.axis('scaled')
plt.show()