import matplotlib.pyplot as plt
import numpy as np


def draw_spiral_grid_with_colors(n, m):
    x = np.linspace(0, 1, m + 1)
    y = np.linspace(0, 1, n + 1)

    colors = plt.cm.rainbow(np.linspace(0, 1, (n) * (m+1)))

    fig, ax = plt.subplots()
    hh = 0
    for layer in range(min(n, m) // 2 + min(n, m) % 2):
        for j in range(layer, m - layer):
            color = colors[hh]
            ax.add_patch(plt.Rectangle((x[j], y[layer]), x[j + 1] - x[j], y[layer + 1] - y[layer], color=color))
            hh += 1

        for i in range(layer + 1, n - layer):
            color = colors[hh]
            ax.add_patch(
                plt.Rectangle((x[m - layer - 1], y[i]), x[m - layer] - x[m - layer - 1], y[i + 1] - y[i], color=color))
            hh += 1

        for j in range(m - layer - 2, layer - 1, -1):
            color = colors[hh]
            ax.add_patch(
                plt.Rectangle((x[j], y[n - layer - 1]), x[j + 1] - x[j], y[n - layer] - y[n - layer - 1], color=color))
            hh += 1

        for i in range(n - layer - 2, layer, -1):
            color = colors[hh]
            ax.add_patch(plt.Rectangle((x[layer], y[i]), x[layer + 1] - x[layer], y[i + 1] - y[i], color=color))
            hh += 1

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()


draw_spiral_grid_with_colors(int(input("По горизонтали:")), int(input("По горизонтали:")))
