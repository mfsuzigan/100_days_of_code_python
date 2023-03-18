from turtle import Turtle

from direction import Direction


class SnakeBlock(Turtle):
    def __init__(self, head=None):
        super().__init__()
        self.penup()
        self.shape("square")
        self.tail = None
        self.block_id = 0

        if head is None:
            self.setx(0)
            self.sety(0)
            self.color("white")

        else:
            self.head = head
            self.block_id = head.block_id + 1
            head.tail = self

            self.shape(head.shape())
            self.color(head.pencolor())

            self.setx(self.head.xcor() - 20)
            self.sety(self.head.ycor())

    def move_to_position(self, x_pos, y_pos):
        x_prev = self.xcor()
        y_prev = self.ycor()

        self.setx(x_pos)
        self.sety(y_pos)
        self.print_position()

        if self.tail is not None:
            self.tail.move_to_position(x_prev, y_prev)

    def move_to_direction(self, direction: Direction):
        x_prev = self.xcor()
        y_prev = self.ycor()

        self.setx(self.xcor() + direction.x_mov)
        self.sety(self.ycor() + direction.y_mov)
        self.print_position()

        if self.tail is not None:
            self.tail.move_to_position(x_prev, y_prev)

    def print_position(self):
        print(f"Block {self.block_id} moved to ({self.xcor()}, {self.ycor()})")
        # input()
