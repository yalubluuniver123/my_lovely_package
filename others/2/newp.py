import turtle

# Функция для рисования равностороннего треугольника
def draw_equilateral_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Очистить предыдущий рисунок
turtle.reset()

# Задаем размеры квадрата
square_side_length = 100

# Рисуем квадрат
turtle.penup()
turtle.pendown()
for _ in range(4):
    turtle.forward(square_side_length)
    turtle.right(90)

# Находим координаты вершин вписанного в квадрат треугольника
triangle_side_length = square_side_length * (2 ** 0.5) / 2  # Длина стороны треугольника
triangle_height = triangle_side_length * (3 ** 0.5) / 2  # Высота треугольника

# Рисуем равносторонний треугольник внутри квадрата
turtle.right(90)
turtle.forward(square_side_length)
turtle.left(90)
turtle.forward(square_side_length/2)
turtle.setheading(60)
draw_equilateral_triangle(square_side_length)
turtle.forward(square_side_length/2)
turtle.circle(square_side_length/4)

turtle.left(120)
turtle.forward(square_side_length/4)

# Завершаем программу по клику
turtle.exitonclick()
