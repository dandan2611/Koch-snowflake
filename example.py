from turtle import Turtle

turtle = Turtle()


def vonKoch(n, length):
    if n == 0:
        turtle.forward(length)
        return

    vonKoch(n - 1, length / 3)
    turtle.left(60)
    vonKoch(n - 1, length / 3)
    turtle.right(120)
    vonKoch(n - 1, length / 3)
    turtle.left(60)
    vonKoch(n - 1, length / 3)


turtle.speed(0)
turtle.penup()
turtle.setposition(-100, -100)
turtle.pendown()

vonKoch(3, 200)

turtle.getscreen().mainloop()
