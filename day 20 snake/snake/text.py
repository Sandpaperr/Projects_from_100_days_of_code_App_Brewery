from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.hightscore_file_name = r"snake\hightscore.txt"
        with open(self.hightscore_file_name) as file:
            self.hightscore = int(file.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.hightscore}", move=False, align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.hightscore:
            self.hightscore = self.score
            self.write_hightscore()
        self.score = 0
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def write_hightscore(self):
        with open(self.hightscore_file_name, "w") as file:
            file.write(f"{self.hightscore}")