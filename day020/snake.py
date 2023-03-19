from turtle import Screen

from snake_block import SnakeBlock


class Snake:

    def __init__(self, screen: Screen):
        self.screen = screen

        self.head = SnakeBlock(head=None)
        body = SnakeBlock(head=self.head)

        for _ in range(0, 8):
            block = SnakeBlock(head=body)
            body = block

        self.update_controls()

    def add_block(self, block: SnakeBlock):
        self.head.add_block(block)

    def update_controls(self):
        headings_with_controls = {
            0: {"Up": self.turn_left, "Down": self.turn_right, "Right": None, "Left": None},
            90: {"Up": None, "Down": None, "Right": self.turn_right, "Left": self.turn_left},
            180: {"Up": self.turn_right, "Down": self.turn_left, "Right": None, "Left": None},
            270: {"Up": None, "Down": None, "Right": self.turn_left, "Left": self.turn_right},
        }

        for direction in ["Up", "Down", "Right", "Left"]:
            current_heading = int(self.head.heading())
            self.screen.onkey(key=direction, fun=headings_with_controls[current_heading][direction])

        self.screen.listen()

    def move(self):
        self.head.move()
        self.screen.update()
        self.update_controls()

    def turn_right(self):
        self.head.right(90)
        self.print_heading()
        self.move()

    def turn_left(self):
        self.head.left(90)
        self.print_heading()
        self.move()

    def print_heading(self):
        print(f"Heading is {self.head.heading()}")
