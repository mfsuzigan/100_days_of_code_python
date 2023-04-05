from turtle import Turtle

STARTING_X_POS = 340
BASE_X_INCREMENT = -4


class Car(Turtle):

    def __init__(self, color, y_cor, speed):
        super().__init__()
        self.color(color)
        self.penup()
        self.goto(STARTING_X_POS, y_cor)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed = speed

    def move(self):
        x_increment = BASE_X_INCREMENT * self.speed
        self.goto(self.xcor() + x_increment, self.ycor())

    def collision_detected(self, player: Turtle):
        player_is_in_front_of_car = player.ycor() > (self.ycor() - 20) and (player.ycor() < self.ycor() + 20)
        player_is_too_close = self.distance(player) < 30

        return player_is_in_front_of_car and player_is_too_close
