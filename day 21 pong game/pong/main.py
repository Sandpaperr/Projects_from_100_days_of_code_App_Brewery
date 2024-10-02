# This code is built upon a skeleton provided by App Brewery.
# Modifications and further implementations were done by Leandro.
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

PADDLE_LEFT_POSITION = (-350, 0)
PADDLE_RIGT_POSITION = (350, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width = SCREEN_WIDTH, height= SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Pong game")
screen.tracer(0)

paddle_left = Paddle(PADDLE_LEFT_POSITION)
paddle_right = Paddle(PADDLE_RIGT_POSITION)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(paddle_left.up,"w")
screen.onkeypress(paddle_left.down,"s")
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")

game_is_on = True
y_direction = True #true is positive and false is negative
x_direction = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # bounce wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # bounce paddle
    if ball.distance(paddle_left.position()) < 60 and ball.xcor() < PADDLE_LEFT_POSITION[0] + 29:
        ball.bounce_x()



    if ball.distance(paddle_right.position()) < 60 and ball.xcor() > PADDLE_RIGT_POSITION[0] - 29 and ball.xcor():
        ball.bounce_x()


    if ball.xcor() > PADDLE_RIGT_POSITION[0] + 30:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < PADDLE_LEFT_POSITION[0] -30:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False
        scoreboard.game_over()



screen.exitonclick()