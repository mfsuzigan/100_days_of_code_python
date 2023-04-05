FONT = ("Courier", 18, "normal")
GAME_OVER_FONT = ("Courier", 18, "bold")

from turtle import Turtle

TEXT_ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 265)
        self.display()

    def display(self):
        self.write(arg=f"Level: {self.player_level}", align=TEXT_ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(-65, 0)
        self.write(arg=f"GAME OVER", align=TEXT_ALIGNMENT, font=GAME_OVER_FONT)

    def level_up(self):
        self.player_level += 1
        self.clear()
        self.display()
