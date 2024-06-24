import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
import matplotlib.colors as mcolors
import numpy as np

def generate_colors(num_rectangles):
    cmap = plt.cm.gray  # Используем цветовую карту серого цвета от белого до черного
    norm = mcolors.Normalize(vmin=0, vmax=num_rectangles)  # Нормализуем значения для получения цветов в градиенте
    scalar_map = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    colors = [scalar_map.to_rgba(i) for i in range(num_rectangles)]
    return colors

def draw_snake(rectangles, colors):
    num_rectangles = len(rectangles)
    for i in range(num_rectangles):
        rectangle = rectangles[i]
        color = colors[i]
        if i % 2 == 0:
            plt.fill(*zip(*rectangle), color=color)
        else:
            plt.fill(*zip(*rectangle[::-1]), color=color)

def main_snake(num_horizontal, num_vertical, mode):
    # Создаем прямоугольники
    rectangles = []
    for i in range(num_vertical):
        if i % 2 == 0:
            for j in range(num_horizontal):
                x = [j, j+1, j+1, j]
                y = [i, i, i+1, i+1]
                rectangles.append(list(zip(x, y)))
        else:
            for j in range(num_horizontal-1, -1, -1):
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
    num_horizontal = int(input("Horizontal squares: "))
    num_vertical = int(input("Vertical squares: "))
    mode = 'snake'
    main_snake(num_horizontal, num_vertical, mode)

