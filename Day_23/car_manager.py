from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_car(random.randint(-300, 300), random.randint(-250, 250), 15)

    def create_car(self, x, y, number):
        for _ in range(number):
            new_car = Turtle("square")
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
            new_car.goto(x, y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            x_pos = car.xcor() - MOVE_INCREMENT
            y_pos = car.ycor()
            car.goto(x_pos, y_pos)

    def destroy(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                car.ht()
                self.all_cars.pop(self.all_cars.index(car))
