from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Your score is: {self.score}", align="center", font=FONT)
        self.goto(250, 250)
        self.write(f'{self.lives} lives left', align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -60)
        self.write("Game Over", align='center', font=("Courier", 50, "normal"))

