from turtle import Turtle, Screen

james = Turtle()
screen = Screen()

def move_forward():
    james.forward(10)

def move_backward():
    james.backward(10)

def rotate_left():
    james.setheading(james.heading() + 10)

def rotate_right():
    james.setheading(james.heading() - 10)

def clear_screen():
    james.clear()




screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
