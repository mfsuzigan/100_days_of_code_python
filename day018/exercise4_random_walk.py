from turtle import Turtle
from random import Random

turtle = Turtle()
turtle.pensize(10)
turtle.speed(0)
turtle.getscreen().colormode(255)
random = Random()
possible_angles = [0, 90, 180, 270]

while True:
    turtle.setheading(random.choice(possible_angles))
    turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.forward(20)

turtle.getscreen().exitonclick()
