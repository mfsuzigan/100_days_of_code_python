from turtle import Screen

from snake_block import SnakeBlock

UP_HEADING = 90
DOWN_HEADING = 270
RIGHT_HEADING = 0
LEFT_HEADING = 180


class Snake:

    def __init__(self, screen: Screen):
        self.screen = screen
        self.head = None

        self.add_block(SnakeBlock())
        self.add_block(SnakeBlock())
        self.add_block(SnakeBlock())

        self.setup_controls()

    def add_block(self, block: SnakeBlock):

        if self.head is None:
            self.head = block
            self.head.setx(0)
            self.head.sety(0)

        else:
            self.head.add_block_to_tail(block)

    def setup_controls(self):
        self.screen.onkey(key="Up", fun=self.face_up)
        self.screen.onkey(key="Down", fun=self.face_down)
        self.screen.onkey(key="Right", fun=self.face_right)
        self.screen.onkey(key="Left", fun=self.face_left)
        self.screen.listen()

    def move(self):
        self.head.move()
        self.screen.update()

    def face_up(self):

        if self.head.heading() != DOWN_HEADING:
            self.head.setheading(UP_HEADING)

    def face_down(self):

        if self.head.heading() != UP_HEADING:
            self.head.setheading(DOWN_HEADING)

    def face_right(self):

        if self.head.heading() != LEFT_HEADING:
            self.head.setheading(RIGHT_HEADING)

    def face_left(self):

        if self.head.heading() != RIGHT_HEADING:
            self.head.setheading(LEFT_HEADING)

    def print_heading(self):
        print(f"Heading is {self.head.heading()}")
