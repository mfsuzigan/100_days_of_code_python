import random
from turtle import Turtle


class SnakeFood(Turtle):

    @staticmethod
    def get_min_coordinate(screen_dimension):
        return 0 - (screen_dimension / 2) + 20

    @staticmethod
    def get_max_coordinate(screen_dimension):
        return (screen_dimension / 2) - 20

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.x_range = screen_width
        self.y_range = screen_height
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        self.update_position()

    def update_position(self):
        self.setx(
            random.randint(SnakeFood.get_min_coordinate(self.x_range), SnakeFood.get_max_coordinate(self.x_range)))

        self.sety(
            random.randint(SnakeFood.get_min_coordinate(self.y_range), SnakeFood.get_max_coordinate(self.y_range)))
