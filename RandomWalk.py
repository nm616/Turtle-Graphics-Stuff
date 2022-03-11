import turtle
from turtle import Turtle, Screen
import random

james = Turtle()
james.shape("turtle")
james.color("blue")
james.pensize(20)
james.speed(0)

nigel = Turtle()
nigel.shape("turtle")
nigel.color("pink")
nigel.pensize(20)
nigel.speed(0)

screen = Screen()
screen.screensize(1000,1000)
screen.colormode(255)


walk_steps = 1000

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def random_direction():
    headings = [0, 90, 180, 270]
    return random.choice(headings)

for x in range(walk_steps):
    james.pencolor(random_color())
    nigel.pencolor(random_color())
    james.setheading(random_direction())
    nigel.setheading(random_direction())
    james.forward(25)
    nigel.forward(25)







screen.exitonclick()