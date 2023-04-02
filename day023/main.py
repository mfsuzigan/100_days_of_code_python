from turtle import Screen

from car_manager import CarManager
from player import Player

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600


def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    game_is_on = True

    player = Player()
    car_manager = CarManager(SCREEN_HEIGHT)
    car_manager.add_car()
    car_manager.add_car()
    car_manager.add_car()
    car_manager.start_traffic()


if __name__ == "__main__":
    main()
