# ================================================
# ACTIVITY - COLOURFUL LOOP ARTWORK
# ================================================

# PART 1 - IMPORT AND SCREEN SETUP
# Create the drawing canvas and set its background.

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colourful Loop Artwork")


# PART 2 - CREATE THE TURTLE PEN
# Create a turtle to draw the artwork.

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()


# PART 3 - CREATE A PETAL FUNCTION
# This function draws one filled petal.
# A petal is made using a repeated movement
# and a small turn.

def draw_petal(petal_color):
    board.color(petal_color)
    board.begin_fill()

    for i in range(2):
        board.circle(60, 60)
        board.left(120)

    board.end_fill()


# PART 4 - REPEAT THE PETAL WITH DIFFERENT COLOURS
# The loop rotates the turtle after drawing each petal.
# Different colours are used to create a colourful pattern.

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]

for i in range(12):
    draw_petal(colors[i % len(colors)])
    board.right(30)


# KEEP THE CANVAS WINDOW OPEN
turtle.done()
