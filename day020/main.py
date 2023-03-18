from turtle import Turtle, Screen


class Snake:

    def __init__(self, color):
        self.x_pos = 0
        self.y_pos = 0
        self.blocks = [SnakeBlock(color, 0, 0), SnakeBlock(color, -20, 0), SnakeBlock(color, -40, 0)]

    def draw(self):
        pass


class SnakeBlock(Turtle):
    def __init__(self, color, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setx(x_pos)
        self.sety(y_pos)
        self.color(color)

    def draw(self):
        pass


def main():
    screen = Screen()
    screen.screensize(600, 600)
    screen.bgcolor("black")
    snake = Snake("white")
    screen.exitonclick()


if __name__ == "__main__":
    main()
