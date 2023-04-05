import math
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

SCREEN_REFRESH_INTERVAL_SECONDS = 0.1
STARTING_INTERVAL_BEFORE_ADDING_CARS_SECONDS = 4

LEVEL_UP_SPEED_INCREASE_PERCENTAGE = 10
LEVEL_UP_ADDING_CARS_INTERVAL_DECREASE_PERCENTAGE = 50


def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)

    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()
    car_manager.setup_lanes(SCREEN_HEIGHT)

    game_over = False
    new_cars_cycle_counter = 0
    screen_cycles_before_adding_car = get_screen_cycles_before_adding_car(scoreboard.player_level)
    print_info(scoreboard, car_manager, screen_cycles_before_adding_car)

    while not game_over:
        new_cars_cycle_counter += 1
        game_over = car_manager.go_with_traffic(player) == CarManager.TrafficState.COLLISION

        if player.has_leveled_up():
            scoreboard.level_up()
            screen_cycles_before_adding_car = get_screen_cycles_before_adding_car(scoreboard.player_level)
            car_manager.increase_traffic_speed(percentage=LEVEL_UP_SPEED_INCREASE_PERCENTAGE)

            player.reset_position()

            print_info(scoreboard, car_manager, screen_cycles_before_adding_car)

        if new_cars_cycle_counter >= screen_cycles_before_adding_car:
            car_manager.add_car()
            print("Car added")
            new_cars_cycle_counter = 0

        time.sleep(SCREEN_REFRESH_INTERVAL_SECONDS)
        screen.update()

    if game_over:
        scoreboard.game_over()

    screen.exitonclick()


def get_screen_cycles_before_adding_car(player_level):
    current_interval_before_adding_cars = STARTING_INTERVAL_BEFORE_ADDING_CARS_SECONDS * math.pow(
        LEVEL_UP_ADDING_CARS_INTERVAL_DECREASE_PERCENTAGE / 100,
        player_level)

    return int(current_interval_before_adding_cars / SCREEN_REFRESH_INTERVAL_SECONDS)


def print_info(scoreboard, car_manager, screen_cycles_before_adding_car):
    print(
        f"Player Level {scoreboard.player_level}, "
        f"speed level={car_manager.speed_level}, "
        f"screen cycles before adding car={screen_cycles_before_adding_car}s")


if __name__ == "__main__":
    main()
