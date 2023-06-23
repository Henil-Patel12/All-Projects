import turtle

def draw_star(turt, x, y, size, fill_color):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    for i in range(5):
        turt.forward(size)
        turt.right(144)
        turt.forward(size)
        turt.right(144)
    turt.end_fill()
    turt.penup()

def moving_star():
    turtle.speed(0)
    turtle.colormode(255)
    turtle.hideturtle()
    for i in range(255):
        draw_star(turtle, 0, 0, 100, (i, i, i))
        turtle.right(10)

moving_star()
turtle.done()
