import matplotlib.pyplot as plt
import numpy as np


def draw_square_grid_with_colors(n):
    x = np.linspace(0, 1, n + 1)
    y = np.linspace(0, 1, n + 1)
    xx, yy = np.meshgrid(x, y)
    grid = np.dstack((xx, yy))

    colors = plt.cm.rainbow(np.linspace(0, 1, n * n))

    hh = 0

    fig, ax = plt.subplots()
    for i in range(n):
        if i % 2 == 0:
            start = 0
            end = n
            step = 1
        else:
            start = n - 1
            end = -1
            step = -1

        for j in range(start, end, step):
            color = colors[hh]
            ax.add_patch(plt.Rectangle((x[j], y[i]), x[1] - x[0], y[1] - y[0], color=color))

            hh += 1

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()



n = int(input("N:"))
draw_square_grid_with_colors(n)
