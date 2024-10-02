import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# SCRENN SETUP ######################
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#####################################

# GAME SETUP ################################
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")
###############################################

# GAME #####################################
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    car_manager.create_car()

    # Detect collision
    for car in car_manager.car_list:
        if player.distance(car.position()) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.reseat_turtle()
        car_manager.increase_speed()
        scoreboard.increase_score()
###############################################################

screen.exitonclick() 
