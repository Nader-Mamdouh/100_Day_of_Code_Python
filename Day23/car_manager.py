import random
from turtle import Turtle, Screen
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
YAXiS = [-200,-150,-100,-50,0,50,100,150,200]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        num = random.randint(1,6)
        if num==1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.choice(YAXiS)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
