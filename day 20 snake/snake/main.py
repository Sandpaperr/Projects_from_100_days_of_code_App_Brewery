# This code is built upon a skeleton provided by App Brewery.
# Modifications and further implementations were done by Leandro.
import time
from turtle import Screen
from snake import Snake
from food import Food
from text import Text

## SET UP SCREEN ###################
screen = Screen()

screen.setup(width = 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#################################

## SET UP SNAKE, FOOD AND TEXT ###############
snake = Snake()
food = Food()
text = Text()
###############################################

## LISTENING TO KEYPRESS ####################
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")
###########################################

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collition with other part of the snake
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            text.reset()
            snake.reset()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -279:
        text.reset()
        snake.reset()


    # detecting collision with food

    if snake.head.distance(food) < 15:
        food.refresh()

        # detect food created where the snake is
        food_under_snake = True
        while food_under_snake:
            food_under_snake = False

            for seg in snake.snake_body:
                if food.distance(seg) < 10:
                    food.refresh()
                    food_under_snake = True

        text.increase_score()
        snake.extend()




screen.exitonclick()