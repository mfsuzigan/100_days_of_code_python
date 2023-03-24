from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, min_ycor, max_ycor, control_up_key="Up", control_down_key="Down"):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.width = 20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.hideturtle()
        self.showturtle()
        self.max_ycor = max_ycor
        self.min_ycor = min_ycor

        self.screen.onkey(key=control_up_key, fun=self.move_up)
        self.screen.onkey(key=control_down_key, fun=self.move_down)
        self.screen.listen()

    def move_down(self):

        if self.ycor() >= self.min_ycor:
            self.goto(self.xcor(), self.ycor() - 20)

    def move_up(self):

        if self.ycor() <= self.max_ycor:
            self.goto(self.xcor(), self.ycor() + 20)
