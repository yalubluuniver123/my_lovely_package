import matplotlib.pyplot as plt

# Создаем рисунок и оси
fig, ax = plt.subplots()

# Создаем квадрат
square = plt.Rectangle((0, 0), 1, 1, fill=False)
ax.add_patch(square)

# Определяем координаты вершин равностороннего треугольника
triangle_vertices = [(0.5, 1), (0, 0.5), (1, 0.5)]

# Создаем равносторонний треугольник
triangle = plt.Polygon(triangle_vertices, closed=True, fill=False)
ax.add_patch(triangle)

# Устанавливаем пределы осей
plt.xlim(0, 1)
plt.ylim(0, 1)

# Показываем рисунок
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.show()
