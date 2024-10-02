import random
from turtle import Turtle, Screen


colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def race(list_turtles):
    for turtle in list_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

        if turtle.xcor() >= 220:
            return turtle

    return None



## SET UP SCREEN #################################
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ").lower()
while not user_bet in colors:
    user_bet = screen.textinput(title="Choose a colour ", prompt="Which turtle will win the race? Enter a colour: ").lower()

user_money = screen.textinput(title= "Make your bet", prompt= "How much do you want to bet?: ")
while not user_money.isdigit():
    user_money = screen.textinput(title="Make your bet", prompt="How much do you want to bet?: ")
user_money = float(user_money)

race_is_on = False
####################################################


## SET UP TURTLES #######################################
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)
#########################################################

## RACE #################################################
if user_bet:
    race_is_on = True

while race_is_on:
    winner = race(all_turtles)
    if winner:
        race_is_on = False

print(f"Your choice: {user_bet}")
print(f"Winner: {winner.fillcolor()}")
if winner.fillcolor() == user_bet:
    print(f"Congrats, you won £{user_money}")
else:
    print(f"You loose £{user_money}, try again next time")


###########################################################

screen.exitonclick()