from turtle import Turtle
from random import Random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color


turtle = Turtle()
turtle.pensize(10)
turtle.speed(0)
turtle.getscreen().colormode(255)
random = Random()
possible_angles = [0, 90, 180, 270]

while True:
    turtle.setheading(random.choice(possible_angles))
    turtle.color(random_color())
    turtle.forward(20)
