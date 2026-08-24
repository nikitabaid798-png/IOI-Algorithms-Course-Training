# ================================================
# ACTIVITY - DRAW A SQUARE ON CANVAS
# ================================================

# PART 1 - IMPORT AND SCREEN SETUP
# turtle.Screen() creates the canvas for drawing.
# bgcolor() sets the background color.
# title() gives a name to the drawing window.

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Square Drawing")


# PART 2 - CREATE THE TURTLE PEN
# turtle.Turtle() creates the drawing pen.
# speed("fastest") makes the turtle draw quickly.
# hideturtle() hides the turtle arrow after drawing.

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()


# PART 3 - DRAW THE SQUARE
# The for loop repeats 4 times because a square
# has 4 equal sides.
# forward(100) moves the turtle forward 100 pixels.
# right(90) turns the turtle by 90 degrees.

board.color("cyan")
board.width(3)

for i in range(4):
    board.forward(100)
    board.right(90)


# KEEP THE CANVAS WINDOW OPEN
turtle.done()
