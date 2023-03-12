import random
from turtle import Turtle

# extracted via colorgram
color_list = [(208, 160, 82), (55, 89, 132), (145, 91, 40), (139, 26, 48), (222, 207, 105), (132, 176, 203),
              (45, 55, 104), (158, 46, 84), (169, 159, 40), (128, 189, 143), (84, 20, 44), (38, 43, 66), (187, 93, 106),
              (188, 138, 167), (84, 123, 182), (59, 39, 30), (79, 153, 165), (88, 157, 90), (195, 80, 71),
              (159, 201, 220), (79, 74, 43), (45, 74, 77), (59, 127, 118), (218, 176, 187), (167, 207, 165),
              (179, 188, 212)]

turtle = Turtle()
turtle.getscreen().colormode(255)
turtle.penup()
turtle.hideturtle()
turtle.setx(-100)
turtle.sety(-100)

for y_move in range(10):

    for x_move in range(1, 11):
        turtle.dot(20, random.choice(color_list))

        if x_move % 10 != 0:
            turtle.forward(50)

        else:
            turtle.setheading(90)
            turtle.forward(50)

    if y_move % 2 == 0:
        turtle.setheading(180)

    else:
        turtle.setheading(0)

turtle.getscreen().exitonclick()
