from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_back():
    turtle.back(10)


def turn_left():
    turtle.setheading(turtle.heading() + 30)


def turn_right():
    turtle.setheading(turtle.heading() - 30)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


actions_by_key = {"w": move_forward, "s": move_back, "a": turn_left, "d": turn_right, "c": clear_screen}

for key in actions_by_key:
    screen.onkey(fun=actions_by_key[key], key=key)

screen.listen()
screen.exitonclick()
