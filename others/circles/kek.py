import numpy as np
from matplotlib import pyplot as plt


def draw_circle(num_sectors):
    colors = plt.cm.viridis(np.linspace(0, 1, num_sectors))
    angles = np.linspace(0, 2*np.pi, num_sectors+1)
    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(aspect='equal'))
    for i in range(num_sectors):
        theta = np.linspace(angles[i], angles[i+1], 100)
        x = np.concatenate([[0], np.cos(theta), [0]])
        y = np.concatenate([[0], np.sin(theta), [0]])
        ax.fill(x,y,color=colors[i],edgecolor='black')

    plt.show()

draw_circle(5)