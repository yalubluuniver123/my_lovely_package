import matplotlib.pyplot as plt
import numpy as np


def draw_colored_circle(num_sectors):
    # Проверка числа секторов
    if not (3 <= num_sectors <= 10):
        raise ValueError("Количество секторов должно быть в диапазоне от 3 до 10.")

    # Создание цветов для секторов
    colors = plt.cm.viridis(np.linspace(0, 1, num_sectors))

    # Углы для секторов
    angles = np.linspace(0, 2 * np.pi, num_sectors + 1)

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

    # Рисование секторов
    for i in range(num_sectors):
        theta = np.linspace(angles[i], angles[i + 1], 100)
        x = np.concatenate([[0], np.cos(theta), [0]])
        y = np.concatenate([[0], np.sin(theta), [0]])
        ax.fill(x, y, color=colors[i], edgecolor='black')

    # Убрать оси
    ax.axis('off')

    plt.show()

# Вызов функции для отрисовки круга с секторами
draw_colored_circle(5)  # Пример вызова функции с 5 секторами
