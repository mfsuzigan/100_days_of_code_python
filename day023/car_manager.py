import random
import time
from turtle import Screen

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_WIDTH = 30
CAR_SHOWING_UP_INTERVAL_SECONDS = 1
SCREEN_REFRESH_INTERVAL_SECONDS = 0.1


class CarManager:

    def __init__(self):
        self.screen = Screen()
        self.cars = []
        self.lanes_y_cor = []

    def add_car(self):
        car = Car(color=random.choice(COLORS), speed=1, y_cor=random.choice(self.lanes_y_cor))
        self.cars.append(car)

    def setup_lanes(self, screen_height):
        lanes_count = int(screen_height / LANE_WIDTH) - 1

        for lane in range(1, lanes_count):
            lane_y_cor = -250 + (lane * LANE_WIDTH) - (LANE_WIDTH / 2)
            self.lanes_y_cor.append(lane_y_cor)

    def start_traffic(self, player):
        time_counter = 0

        while True:

            for car in self.cars:
                car.move()

                if car.collision_detected(player):
                    return

            new_car_timer = round(time_counter)

            if new_car_timer != 0 and new_car_timer % CAR_SHOWING_UP_INTERVAL_SECONDS == 0:
                self.add_car()
                time_counter = 0

            time.sleep(SCREEN_REFRESH_INTERVAL_SECONDS)
            time_counter += SCREEN_REFRESH_INTERVAL_SECONDS
            self.screen.update()
