from turtle import Turtle

turtle = Turtle()
pen_is_down = True

for _ in range(0, 100):
    turtle.forward(5)

    if turtle.isdown():
        turtle.penup()

    else:
        turtle.pendown()

turtle.getscreen().exitonclick()
