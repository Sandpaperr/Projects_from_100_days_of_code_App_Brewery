from turtle import Turtle
from random import randrange, choice


turtle = Turtle()
turtle.speed("fastest")

def rand_color():
    r = randrange(255.0)
    g = randrange(255.0)
    b = randrange(255.0)
    return [r, g, b]


##### SHAPES #################
def draw_shape(number_of_sides):
    ## RANDOM COLOR
    turtle.pencolor(rand_color())

    ## DRAW SHAPE
    for repeat in range(number_of_sides):
        turtle.right(360 / number_of_sides)
        turtle.forward(100)

#########################################

###### RANDOM WALK ######################

def set_direction(angle_dimention):
    angle = randrange(0, 361, angle_dimention)
    turtle.setheading(angle)

########################################

####### DRAW SPIROGRAPH ##################
def draw_spirograph(space_between_circles):
    for angle in range(0, 361, space_between_circles):
        turtle.color(rand_color())
        turtle.setheading(angle)
        turtle.circle(100)
##########################################
