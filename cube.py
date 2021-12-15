# Line.py

# Import libraries
from turtle import Screen, Turtle

# Von Koch
N = 4
AUTO_LENGTH = True  # Calculate automatically the length
AUTO_LENGTH_PER_N = 2
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
screen.title("Flocon de Koch (3)")

# Turtle setup
turtle = Turtle()
if AUTO_LENGTH:
    LENGTH = 250 if N < 4 else 250 + N * AUTO_LENGTH_PER_N
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
    turtle.left(90)
    vonKoch(lowerN, splittedLength)
    turtle.right(90)
    vonKoch(lowerN, splittedLength)
    turtle.right(90)
    vonKoch(lowerN, splittedLength)
    vonKoch(lowerN, splittedLength)
    turtle.left(90)
    vonKoch(lowerN, splittedLength)
    turtle.left(90)
    vonKoch(lowerN, splittedLength)
    turtle.right(90)
    vonKoch(lowerN, splittedLength)


# Begin -- Drawing

turtle.penup()
turtle.setpos(-SCREEN_WIDTH/2, 0)
turtle.pendown()
vonKoch(N, LENGTH)

# End -- Drawing

# Run main loop

screen.mainloop()  # On demande à notre librairie de garder la page ouverte