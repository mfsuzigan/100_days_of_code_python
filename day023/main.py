from turtle import Screen

from car_manager import CarManager
from player import Player

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600


def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)

    player = Player()

    car_manager = CarManager()
    car_manager.setup_lanes(SCREEN_HEIGHT)
    car_manager.start_traffic()
    screen.exitonclick()


if __name__ == "__main__":
    main()
