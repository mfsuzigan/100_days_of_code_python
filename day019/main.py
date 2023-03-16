import random
import time
from turtle import Turtle, Screen


class RaceTurtle(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.x_final = 0
        self.finished_at = 0

    def setup(self, x_start, y_start, x_final):
        self.penup()
        self.setx(x_start)
        self.sety(y_start)
        self.x_final = x_final

    def move(self):

        if self.xcor() < self.x_final:
            step = random.randint(0, 25)
            self.forward(step)
            self.screen.ontimer(self.move, 250)

        elif self.finished_at == 0:
            self.finished_at = time.time_ns()
            print(f"Turtle {self.pencolor()} finished at {self.finished_at:.0f}")
            check_finish_line(self)


finish_line = []
winner_bet = None
turf = [RaceTurtle("red"), RaceTurtle("orange"), RaceTurtle("goldenrod"), RaceTurtle("green"), RaceTurtle("blue"),
        RaceTurtle("purple")]


def check_finish_line(turtle):
    finish_line.append(turtle)

    if len(finish_line) == len(turf):
        winner = finish_line[0]
        print(f"\nRace over!\n\nThe winner 🏆 is: ✨ {winner.pencolor()} turtle ✨")

        if winner_bet == winner.pencolor():
            print("\nYou guessed it right! ✅")

        else:
            print("\nBetter luck next time! ❌ ")


def main():
    screen = Screen()
    screen.setup(width=640, height=480)

    for turtle in turf:
        # evenly spacing turtles vertically
        start_y_pos = 210 - turf.index(turtle) * 70
        # final x considering that turtle is a40x40 object
        turtle.setup(x_start=-310, y_start=start_y_pos, x_final=290)

    global winner_bet
    color_list = [turtle.pencolor() for turtle in turf]
    winner_bet = str.lower(screen.textinput("Make your bet ☘️",
                                            f"Which turtle will win the race? ({str.join(', ', color_list)})"))
    print(f"User's bet ☘️  for winning turtle is: {winner_bet}")

    for turtle in turf:
        screen.ontimer(turtle.move, 250)

    screen.exitonclick()


if __name__ == "__main__":
    main()
