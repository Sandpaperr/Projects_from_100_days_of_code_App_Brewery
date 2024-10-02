import random
import turtle

import functions_turtle as ft
from turtle import Turtle, Screen

list_colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
               (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
               (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
               (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

## SET UP
bella = ft.turtle
turtle.colormode(255)
bella.penup()
bella.goto(-225, -225)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    bella.dot(20, random.choice(list_colors))
    bella.forward(50)

    if dot_count % 10 == 0:
        bella.setheading(90)
        bella.forward(50)
        bella.setheading(180)
        bella.forward(500)
        bella.setheading(0)
















screen = Screen()
screen.exitonclick()
