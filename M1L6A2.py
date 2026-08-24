# ================================================
# ACTIVITY - DRAW A STAR ON CANVAS
# ================================================

# PART 1 - IMPORT AND SCREEN SETUP
# turtle.Screen() creates the canvas.
# bgcolor() sets the background color.
# title() gives a name to the drawing window.

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star Drawing")


# PART 2 - CREATE THE TURTLE PEN
# turtle.Turtle() creates the drawing pen.
# speed("fastest") makes the turtle draw quickly.
# hideturtle() hides the turtle arrow.

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()


# PART 3 - DRAW THE STAR
# A 5-pointed star has 5 sides.
# The loop repeats 5 times.
# forward(150) moves the turtle forward.
# right(144) creates the correct angle for a star.

board.color("yellow")
board.width(3)

for i in range(5):
    board.forward(150)
    board.right(144)


# KEEP THE CANVAS WINDOW OPEN
turtle.done()
