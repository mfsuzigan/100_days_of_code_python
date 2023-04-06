from turtle import Turtle


class SnakeBlock(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.head = None
        self.tail = None
        self.id = 0

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

    def add_block_to_tail(self, block):

        if self.tail is None:
            self.tail = block
            block.setx(self.xcor() - 20)
            block.sety(self.ycor())
            print(f"Block {block.id} added")

        else:
            block.id += 1
            self.tail.add_block_to_tail(block)
