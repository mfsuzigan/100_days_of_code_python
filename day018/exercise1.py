from turtle import Turtle

turtle = Turtle()

for _ in range(0, 4):
    turtle.forward(100)
    turtle.right(90)

turtle.getscreen().exitonclick()
