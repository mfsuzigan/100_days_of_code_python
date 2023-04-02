import time
from turtle import Screen

from car import Car
from player import Player


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    game_is_on = True

    player = Player()
    car = Car(color="green", y_cor=150, speed=1)

    while game_is_on:
        car.move()
        time.sleep(0.1)
        screen.update()


if __name__ == "__main__":
    main()
