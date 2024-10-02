from turtle import Turtle
import random
BALL_SIZE = 1
BALL_MOVE = 10 #how many pixels it moves per loop
BALL_SPEED = 0.05 #seconds between 1 move and another
ACCELLERATION = 0.9 #mutiply to ball speed
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(BALL_SIZE, BALL_SIZE)
        self.goto(0, 0)
        self.x_move = BALL_MOVE
        self.y_move = BALL_MOVE
        self.move_speed = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= ACCELLERATION

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = BALL_SPEED



