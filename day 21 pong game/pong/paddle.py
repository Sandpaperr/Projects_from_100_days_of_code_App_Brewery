from turtle import Turtle

PADDLE_LENGTH = 5
SPEED = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position_for_paddle):
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(0)
        self.turtlesize(PADDLE_LENGTH, 1)
        self.goto(position_for_paddle)

    def up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)
