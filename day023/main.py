import time
from turtle import Screen

from car_manager import CarManager
from player import Player

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
CAR_SHOWING_UP_INTERVAL_SECONDS = 0.5
SCREEN_REFRESH_INTERVAL_SECONDS = 0.1
SCREEN_CYCLES_TO_ADDING_CAR = int(CAR_SHOWING_UP_INTERVAL_SECONDS / SCREEN_REFRESH_INTERVAL_SECONDS)


def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)

    player = Player()

    car_manager = CarManager()
    car_manager.setup_lanes(SCREEN_HEIGHT)

    game_over = False
    new_cars_cycle_counter = 0

    while not game_over:
        game_over = car_manager.go_with_traffic(player) == CarManager.TrafficState.COLLISION

        if new_cars_cycle_counter == SCREEN_CYCLES_TO_ADDING_CAR:
            car_manager.add_car()
            new_cars_cycle_counter = 0

        time.sleep(SCREEN_REFRESH_INTERVAL_SECONDS)
        new_cars_cycle_counter += 1
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
