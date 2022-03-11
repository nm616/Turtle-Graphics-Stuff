import turtle

import colorgram
from turtle import Turtle, Screen
import random
from tkinter import *

file_number = 0
# Sets turtle object options
james = Turtle()
james.pensize(5)
james.speed(0)
james.hideturtle()
james.turtlesize(0.5)
james.shape("square")
turtle.tracer(0,0)


# Sets screen settings
screen = Screen()
screen.setup(500, 500)
screen.colormode(255)
screen.title("Dot Painter")

# list of rgb colors collected from colorgram
rgb_colors = []

# extracts colors to use in dots
colors = colorgram.extract("Sunset1.jpg", 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

def color_picker():
    return random.choice(rgb_colors)

james.penup()
for x in range(-250,250, 10):
    for y in range(-250, 250, 10):
        james.setpos(y, x)
        james.color(color_picker())
        james.stamp()
        # file_number += 1
        # getscreen = james.getscreen()
        # getscreen.getcanvas().postscript(file=f"HPaint{file_number}.eps")

screen.update()
getscreen = james.getscreen()
getscreen.getcanvas().postscript(file=f"HPaint{file_number}")
# prevents screen from closing without click
screen.exitonclick()
