from turtle import Turtle

turtle = Turtle()

for _ in range(0, 100):
    turtle.forward(5)

    if turtle.isdown():
        turtle.penup()

    else:
        turtle.pendown()

turtle.getscreen().exitonclick()
