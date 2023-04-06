from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 8
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

        self.screen.onkey(key="Up", fun=self.move)
        self.screen.listen()

    def move(self):
        if self.ycor() != FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def has_leveled_up(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)
