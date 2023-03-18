from enum import Enum


class Direction(Enum):
    FORWARD = 20, 0
    LEFT = 0, 20
    RIGHT = 0, -20

    def __init__(self, x_mov, y_mov):
        self.x_mov = x_mov
        self.y_mov = y_mov
