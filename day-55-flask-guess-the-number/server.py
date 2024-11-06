from flask import Flask
import random

random_number = random.randint(0,9)

def add_image(function):
    image = '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3loNTg0d3NyZmR0enB1M3JkdjBrazgyb3pjb3RrOTQ4YTlpM2EycyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41YtZOb9EUABnuqA/giphy.gif" width="480" height="360" style="" frameBorder="0" class="giphy-embed">'
    def wrapper_image():
        return function() + image
    return wrapper_image

def add_h1(function):
    def wrapper_h1(*args, **kwargs):
        return "<h1>" + function(*args, **kwargs) + "</h1>"
    return wrapper_h1

# add image and text color to the result page
def decoration_guess_number(function):
    def wrapper_function(*args, **kwargs):
        global random_number
        color = "black"
        if kwargs["number"] == random_number:
            image = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
            color = "green"
        elif kwargs["number"] > random_number:
            image = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
            color = "purple"
        else:
            image = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
            color = "red"

        return f'<p style="color: {color};">' + function(*args, **kwargs) + "</p>" + f'<img src={image} width="480" height="360" style="" frameBorder="0" class="giphy-embed">'
    return wrapper_function
        
        

app = Flask(__name__)

@app.route("/")
@add_image
@add_h1
def home():
    global random_number 
    if random_number is None: random_number = random.randint(0, 9)
    return "Guess a number between 0 and 9"

@app.route("/<int:number>")
@add_h1
@decoration_guess_number
def guess_number(number):
    global random_number
    if random_number == number:
        return "You Found the number!"
    elif random_number < number:
        return "Too high, try again!"
    else:
        return "Too low, try again!"



if __name__ == "__main__":
    app.run(debug=True)

