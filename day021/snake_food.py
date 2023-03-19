import random
from turtle import Turtle


class SnakeFood(Turtle):

    @staticmethod
    def get_min_coordinate(screen_dimension):
        return 0 - (screen_dimension / 2) + 20

    @staticmethod
    def get_max_coordinate(screen_dimension):
        return (screen_dimension / 2) + 20

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.setx(
            random.randint(SnakeFood.get_min_coordinate(screen_width), SnakeFood.get_max_coordinate(screen_width)))

        self.sety(
            random.randint(SnakeFood.get_min_coordinate(screen_height), SnakeFood.get_max_coordinate(screen_height)))

        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
