from turtle import Turtle
import utils

turtle = Turtle()
turtle.speed(0)
turtle.getscreen().colormode(255)

for i in range(0, 361, 3):
    turtle.circle(100)
    turtle.color(utils.random_color())
    turtle.setheading(i)

turtle.getscreen().exitonclick()
