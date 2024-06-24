def draw_shape(side_length, iterations):
    import turtle

    def rotate(length):
        turtle.speed(0)
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(length / 2)
        turtle.setheading(180)
        turtle.forward(length / 2)
        turtle.setheading(0)
        turtle.pendown()

    def draw_square(length):
        turtle.color("red")
        for i in range(4):
            turtle.forward(length)
            turtle.right(90)

    def draw_triangle(length):
        turtle.color("blue")
        for i in range(3):
            turtle.forward(length)
            turtle.right(120)

    def draw_circle(radius):
        turtle.circle(radius)

    turtle.speed(0)
    rotate(side_length)
    for _ in range(iterations):
        draw_square(side_length)
        turtle.penup()
        turtle.forward(side_length / 2)
        turtle.right(60)
        turtle.pendown()
        draw_triangle(side_length)
        turtle.right(60)
        turtle.forward(side_length / 2)
        r = (side_length * (3 ** (0.5))) / 6
        turtle.color("green")
        turtle.circle(r, 705)
        turtle.setheading(0)

        side_length = (2 ** 0.5) * r

    turtle.done()


def main():
    side_length = int(input("Сторона квадрата: "))
    iterations = int(input("Сколько вложений: "))

    if iterations > 4:
        print("Превышено кол-во вложений")
        iterations = 4

    draw_shape(side_length, iterations)


if __name__ == '__main__':
    main()
