import colorsys
import turtle

povorot = [1, 2, 4, 6, 9, 12, 16, 20, 25, 30, 36, 42, 49, 56, 64, 72, 81, 90, 100, 110, 121, 132, 144, 156, 169, 182,
           196, 210, 225, 240, 256, 272, 289, 306, 324, 342, 361, 380, 400, 420, 441, 462, 484, 506, 529, 552, 576, 600,
           625, 650, 676, 702, 729, 756, 784, 812, 841, 870, 900, 930, 961, 992, 1024, 1056]


def draw_square(side_length, hue):
    turtle.fillcolor(colorsys.hsv_to_rgb(hue, 1, 1))
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()


def draw_spiral(num_squares, initial_side_length):
    hue = 0
    for i in range(num_squares):
        if i in povorot:
            print(i)
            turtle.forward(initial_side_length)
            turtle.right(90)
        draw_square(initial_side_length, hue)
        turtle.forward(initial_side_length)
        hue += 1 / num_squares


turtle.speed(0)


num_squares = int(input("Number of squares: "))
draw_spiral(num_squares, 50)

turtle.done()
