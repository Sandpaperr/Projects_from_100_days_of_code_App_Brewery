from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)
        self.level = 1
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= "center", font= FONT)
