from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ('Courier', 20, "bold")


def load_high_score():
    with open("game_data.dat", "a+") as game_data:
        game_data.seek(0)

        for line in game_data.readlines():
            key, value = line.strip().split('=')

            if key == "high_score":
                return int(value.strip())

    return 0


def save_high_score(high_score):
    with open("game_data.dat", "r") as game_data:
        file_values = dict([line.strip().split("=") for line in game_data.readlines()])

    file_values["high_score"] = high_score

    with open("game_data.dat", "w") as game_data:
        for key in file_values:
            game_data.write(f"{key}={file_values[key]}\n")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = load_high_score()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.pencolor("white")
        self.display()

    def display(self):
        self.write(arg=f"Score: {self.score}   High score: {self.high_score}", align=TEXT_ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            save_high_score(self.score)

        self.score = 0
        self.clear()
        self.display()

    def increment(self):
        self.score += 1
        self.clear()
        self.display()
