import random
from enum import Enum
from turtle import Screen

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_WIDTH = 30


class CarManager:
    class TrafficState(Enum):
        NORMAL = 0
        COLLISION = 1

    def __init__(self):
        self.screen = Screen()
        self.cars = []
        self.lanes_y_cor = []
        self.speed_level = 1

    def add_car(self):
        car = Car(color=random.choice(COLORS), speed=1, y_cor=random.choice(self.lanes_y_cor))
        self.cars.append(car)

    def setup_lanes(self, screen_height):
        lanes_count = int(screen_height / LANE_WIDTH) - 2

        for lane in range(1, lanes_count):
            lane_y_cor = -250 + (lane * LANE_WIDTH) - (LANE_WIDTH / 2)
            self.lanes_y_cor.append(lane_y_cor)

    def go_with_traffic(self, player):

        for car in self.cars:
            car.move()

            if car.collision_detected(player):
                return CarManager.TrafficState.COLLISION

        return CarManager.TrafficState.NORMAL

    def increase_traffic_speed(self, percentage):
        self.speed_level *= 1 + percentage / 100

        for car in self.cars:
            car.increase_speed(percentage)
