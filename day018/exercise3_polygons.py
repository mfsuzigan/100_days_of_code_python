from turtle import Turtle
from random import Random
import utils

turtle = Turtle()
turtle.getscreen().colormode(255)
random = Random()

for number_of_angles in range(3, 11):
    angle_shift = 360 / number_of_angles
    turtle.pencolor(utils.random_color())

    for i in range(number_of_angles):
        turtle.setheading(angle_shift * i)
        turtle.forward(100)

turtle.getscreen().exitonclick()
