import matplotlib.pyplot as plt

def generate_colors(num_rectangles):
    center_color = (0, 0, 0)  # Черный цвет в центре
    edge_color = (1, 1, 1)  # Белый цвет на краях

    colors = []
    for i in range(num_rectangles):
        # Вычисляем значение цвета для текущего прямоугольника на основе его расстояния от центра
        distance_from_center = abs(i - num_rectangles / 2) / (num_rectangles / 2)
        # Интерполируем цвет между черным и белым в зависимости от расстояния до центра
        color = tuple(c_center * (1 - distance_from_center) + c_edge * distance_from_center
                      for c_center, c_edge in zip(center_color, edge_color))
        colors.append(color)
    return colors


def main(num_horizontal, num_vertical):
    # Создаем прямоугольники
    rectangles = []
    for i in range(num_vertical):
        for j in range(num_horizontal):
            x = [j, j+1, j+1, j]
            y = [i, i, i+1, i+1]
            rectangles.append(list(zip(x, y)))

    # Генерируем цвета
    colors = generate_colors(len(rectangles))

    # Рисуем прямоугольники с соответствующими цветами
    for rectangle, color in zip(rectangles, colors):
        plt.fill(*zip(*rectangle), color=color)

    # Настраиваем оси
    plt.axis('equal')
    plt.axis('off')

    # Показываем рисунок
    plt.show()

if __name__ == "__main__":
    num_horizontal = 10
    num_vertical = 10
    main(num_horizontal, num_vertical)
