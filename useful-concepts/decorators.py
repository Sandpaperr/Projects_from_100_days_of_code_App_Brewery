import time

#Decorators are functions that gives additional functionality to an existent function
def delay_decorator(function):
    def wrapped_function():
        #add something before the function
        time.sleep(2)
        function()
        #add something after the function
    return wrapped_function


# What if I want to add an addition functionality to lots of different functions?

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")


def say_greetings():
    print("How are you?")


say_hello()
say_greetings()