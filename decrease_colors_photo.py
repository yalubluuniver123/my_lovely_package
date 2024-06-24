import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


def change_image_colors(image_path, num_colors):
    img = Image.open(image_path)
    img_array = np.array(img)

    h, w, _ = img_array.shape

    pixels = img_array.reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)

    labels = kmeans.labels_
    new_pixels = colors[labels].reshape((h, w, 3))

    new_img = Image.fromarray(new_pixels.astype('uint8'))
    return new_img


def main():
    image_path = "priroda_kartinki_foto_03.jpg"
    num_colors = int(input("Количество цветов:"))

    new_image = change_image_colors(image_path, num_colors)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('До')
    plt.imshow(Image.open(image_path))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title(f'После ({num_colors} цветов)')
    plt.imshow(new_image)
    plt.axis('off')

    plt.show()


if __name__ == '__main__':
    main()
