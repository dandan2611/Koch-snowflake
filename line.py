# Line.py

# Import libraries
from turtle import Screen, Turtle

# Von Koch
N = 8
AUTO_LENGTH = True  # Calculate automatically the length
AUTO_LENGTH_PER_N = 100
LENGTH = 400

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SHOW_TURTLE = False
ENABLE_LEGACY_SPEED = False
TURTLE_SPEED = 0  # speed -> 0 (fastest) < TURTLE_SPEED < 10 (slowest)

# Apply settings

# Screen setup
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Flocon de Koch (1)")

# Turtle setup
turtle = Turtle()
if AUTO_LENGTH:
    LENGTH = 400 if N < 4 else 400 + N * AUTO_LENGTH_PER_N
    if LENGTH > SCREEN_WIDTH:
        LENGTH = SCREEN_WIDTH
if not SHOW_TURTLE:
    turtle.hideturtle()
if ENABLE_LEGACY_SPEED:
    turtle.speed(TURTLE_SPEED)
else:
    turtle.speed(0)
    screen.tracer(2)


# Utils functions

def vonKoch(n, length):
    if n == 0:
        turtle.forward(length)
        return

    splittedLength = length / 3
    lowerN = n - 1

    vonKoch(lowerN, splittedLength)
    turtle.left(60)  # On pivote de 60 degrés vers la gauche (triangle équilatéral)
    vonKoch(lowerN, splittedLength)
    turtle.right(120)
    vonKoch(lowerN, splittedLength)
    turtle.left(60)
    vonKoch(lowerN, splittedLength)


# Begin -- Drawing

turtle.penup()
turtle.setpos(-LENGTH / 2, -300)
turtle.pendown()

vonKoch(N, LENGTH)

# End -- Drawing

# Run main loop

screen.mainloop()  # On demande à notre librairie de garder la page ouverte