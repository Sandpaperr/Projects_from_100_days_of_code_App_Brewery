import turtle
import pandas
import os

FILE_STATES = os.path.join(os.getcwd(), "day 25 usa states", "us-states-game-start","50_states.csv")
FILE_STATES_TO_LEARN = os.path.join(os.getcwd(), "day 25 usa states", "us-states-game-start","states_to_learn.csv")


screen = turtle.Screen()
screen.title("U.S.A States Game")
image = os.path.join(os.getcwd(), "day 25 usa states","us-states-game-start",  "blank_states_img.gif") 
screen.addshape(image)
turtle.shape(image)

data_states = pandas.read_csv(FILE_STATES)

states = data_states.state.to_list()
guess_states = []


while len(guess_states) < 50:

    answer_state = screen.textinput(title=f"{len(guess_states)}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guess_states]
        data_to_store = pandas.DataFrame(missing_states)
        data_to_store.to_csv(FILE_STATES_TO_LEARN)
        break
    if answer_state in states:
        guess_states.append(answer_state)
        turtle_country = turtle.Turtle()
        turtle_country.penup()
        turtle_country.hideturtle()
        state_to_write = data_states[data_states.state == answer_state]
        turtle_country.goto(int(state_to_write.x), int(state_to_write.y))
        turtle_country.write(answer_state)


