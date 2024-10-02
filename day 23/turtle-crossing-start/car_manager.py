from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.create_car()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_y = random.randrange(-260, 280, 20)
            new_car.goto(320, new_y)
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.setx(car.xcor() - self.speed)

            if car.xcor() < -320:
                self.car_list.remove(car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
