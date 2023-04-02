import random
import time
from turtle import Screen

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_WIDTH = 30


class CarManager:

    def __init__(self, screen_height):
        self.cars = []
        self.lanes_y_cor = []
        lanes_count = int(screen_height / LANE_WIDTH)

        for lane in range(1, lanes_count + 1):
            y = -300 + (lane * LANE_WIDTH) - (LANE_WIDTH / 2)
            self.lanes_y_cor.append(y)

    def add_car(self):
        car = Car(color=random.choice(COLORS), speed=1, y_cor=random.choice(self.lanes_y_cor))
        self.cars.append(car)

    def start_traffic(self):
        screen = Screen()

        while True:

            for car in self.cars:
                car.move()

            time.sleep(0.1)
            screen.update()
