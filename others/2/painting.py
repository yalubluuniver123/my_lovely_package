import tkinter as tk
import math

import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'

def draw_shapes(canvas, x, y, size):
    # Рисуем квадрат
    canvas.create_rectangle(x - size/2, y - size/2, x + size/2, y + size/2)

    # Находим координаты вершин равностороннего треугольника
    triangle_height = math.sqrt(3) * size / 2
    triangle_points = [
        (x - size/2, y + triangle_height/2),
        (x + size/2, y + triangle_height/2),
        (x, y - triangle_height/2)
    ]
    # Рисуем треугольник
    canvas.create_polygon(triangle_points, outline='black')

    # Рисуем окружность
    circle_radius = size / 2
    canvas.create_oval(x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius, outline='black')

def draw_nested_shapes(canvas, x, y, size, iterations):
    if iterations == 0:
        return

    draw_shapes(canvas, x, y, size)

    # Находим координаты центра круга
    circle_center = (x, y)
    # Рекурсивно рисуем вложенные фигуры
    draw_nested_shapes(canvas, *circle_center, size / 2, iterations - 1)

def main(square_size, iterations):
    # Создаем окно Tkinter
    root = tk.Tk()
    root.title("Nested Shapes")

    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()

    # Вызываем функцию для рисования вложенных фигур
    draw_nested_shapes(canvas, 300, 300, square_size, iterations)

    root.mainloop()

# Запускаем программу с пользовательскими параметрами
main(400, 4)
