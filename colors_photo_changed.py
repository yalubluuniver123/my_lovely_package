from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


def change_image_colors(image_path, num_colors):
    image = Image.open(image_path)

    image_np = np.array(image)
    pixels = image_np.reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    new_colors = kmeans.cluster_centers_.astype(int)

    labels = kmeans.predict(pixels)
    new_pixels = new_colors[labels]

    new_image_np = new_pixels.reshape(image_np.shape)
    new_image = Image.fromarray(new_image_np.astype('uint8'), 'RGB')

    return new_image


image_path = 'images.jpeg'
num_colors = int(input("Colors: "))

new_image = change_image_colors(image_path, num_colors)
new_image.show()
