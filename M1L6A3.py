# ================================================
# ACTIVITY - DRAW A RAINBOW SPIRAL
# ================================================

# PART 1 - IMPORT AND SCREEN SETUP
# turtle.Screen() creates the canvas.
# bgcolor() sets the background color.
# title() gives a name to the drawing window.

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Spiral")


# PART 2 - CREATE THE TURTLE PEN
# turtle.Turtle() creates the drawing pen.
# speed("fastest") makes the turtle draw quickly.
# hideturtle() hides the turtle arrow.

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()


# PART 3 - CREATE A LIST OF RAINBOW COLORS
# The colors will be used one after another
# while drawing the spiral.

rainbow_colors = ["red", "orange", "yellow", "green",
                  "blue", "indigo", "violet"]


# PART 4 - DRAW THE RAINBOW SPIRAL
# The loop repeats the drawing steps many times.
# The distance increases with every turn,
# making the spiral grow bigger.
# % is used to repeat the colors from the list.

for i in range(80):
    board.color(rainbow_colors[i % len(rainbow_colors)])
    board.width(3)
    board.forward(i * 3)
    board.right(91)


# KEEP THE CANVAS WINDOW OPEN
turtle.done()
