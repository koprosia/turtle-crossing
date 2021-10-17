import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(x=280, y=random.randint(-280,280))
            self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            new_y = car.ycor()
            car.goto(new_x, new_y)
