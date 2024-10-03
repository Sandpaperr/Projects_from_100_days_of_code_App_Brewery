import pandas
import os

FILE = os.path.join(os.getcwd(), "day 25", "squirrel", "squirrel_data.csv" )
data = pandas.read_csv(FILE)
color = data["Primary Fur Color"].to_list()

squirrel_dic = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [color.count("Gray"), color.count("Cinnamon"),color.count("Black")],
}

color_sq_data = pandas.DataFrame(squirrel_dic)
color_sq_data.to_csv("squirrel_color.csv")