from turtle import Turtle, Screen
import random

james = Turtle()
james.shape("turtle")
james.color("pink")
james.pensize(15)
james.speed(0)

screen = Screen()
screen.screensize(1000,1000)
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


def draw_spiro(size_of_gap):
    # for x in range(int(360/size_of_gap)):
    while True:
        james.pencolor(random_color())
        james.circle(100)
        james.setheading(james.heading() + size_of_gap)

draw_spiro(25)

screen.exitonclick()