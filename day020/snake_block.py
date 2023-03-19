from turtle import Turtle


class SnakeBlock(Turtle):
    def __init__(self, head=None):
        super().__init__()
        self.penup()
        self.shape("square")
        self.tail = None

        if head is None:
            self.setx(0)
            self.sety(0)
            self.color("white")

        else:
            self.head = head
            head.tail = self

            self.shape(head.shape())
            self.color(head.pencolor())

            self.setx(self.head.xcor() - 20)
            self.sety(self.head.ycor())

    def move(self):
        x_prev = self.xcor()
        y_prev = self.ycor()

        self.forward(20)

        if self.tail is not None:
            self.tail.move_to_position(x_prev, y_prev)

    def move_to_position(self, x_pos, y_pos):
        x_prev = self.xcor()
        y_prev = self.ycor()

        self.setx(x_pos)
        self.sety(y_pos)

        if self.tail is not None:
            self.tail.move_to_position(x_prev, y_prev)

    def add_block(self, block):
        pass
