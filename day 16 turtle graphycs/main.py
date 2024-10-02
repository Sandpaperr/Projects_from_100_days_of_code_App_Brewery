# This code is built upon a skeleton provided by App Brewery.
# Modifications and further implementations were done by Leandro.

# import turtle
# timmy = turtle.Turtle()
# my_screen = turtle.Screen()
#
#
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name",
                 ["Pikachu", "Squirtle", "Charmender"])

table.add_column("Type",
                 ["Electric", "Water", "Fire"])
table.align = "l"
print(table)