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

# the @decorator is a sintactic sugar, an easier way to write an alternative line of code. 
#The "proper" line is this
decorated_function = delay_decorator(say_greetings)
decorated_function()


#Usings variables in a function from the wrapper function
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s blog post")

new_user = User("Leandro")
new_user.is_logged_in = True
create_blog_post(new_user)