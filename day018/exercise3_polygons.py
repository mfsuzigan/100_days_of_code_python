from turtle import Turtle
from random import Random

turtle = Turtle()
turtle.getscreen().colormode(255)
random = Random()

for number_of_angles in range(3, 11):
    angle_shift = 360 / number_of_angles
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    for i in range(number_of_angles):
        turtle.setheading(angle_shift * i)
        turtle.forward(100)

turtle.getscreen().exitonclick()
