import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000,height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_choice = screen.textinput(title="Pick a Turtle", prompt="Pick a turtle! Enter a color: \n"
                                                             "Red|Orange|Yellow|Green|Blue|Purple" )


x_cord = -480
y_cord = -100
all_turtles = []

for x in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(0)
    new_turtle.penup()
    new_turtle.color(x)
    new_turtle.goto(x=x_cord, y=y_cord)
    y_cord += 40
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.pendown()
        turtle.width(5)
        if turtle.xcor() > 480:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice.lower():
                print(f"You Won! {winning_color.title()} won!")
            else:
                print(f"You Lost! {winning_color.title()} won!")
        random_distance = random.randint(1, 15)
        turtle.forward(random_distance)

screen.exitonclick()
