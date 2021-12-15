from turtle import Turtle

turtle = Turtle()


def vonKoch(n, length):
    if n == 0:
        turtle.forward(length)
        return

    splittedLength = length / 3
    lowerN = n - 1

    vonKoch(lowerN, splittedLength)
    turtle.left(60)  # On pivote de 60 degrés vers la gauche (triangle isocèle)
    vonKoch(lowerN, splittedLength)
    turtle.right(120)
    vonKoch(lowerN, splittedLength)
    turtle.left(60)
    vonKoch(lowerN, splittedLength)


turtle.speed(0)
turtle.penup()
turtle.setposition(-100, -100)
turtle.pendown()

vonKoch(3, 200)

turtle.getscreen().mainloop()
