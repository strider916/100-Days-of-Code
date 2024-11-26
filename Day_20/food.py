from turtle import Turtle
import random
FOOD_POS = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100,
            120, 140, 160, 180, 200, 220, 240, 260, 280]


class Food:
    def __init__(self):
        self.food = Turtle(shape="circle")
        self.food.color("aquamarine")
        self.food.width(1)
        self.food.pu()

    def rand_pos(self):
        xcor = random.choice(FOOD_POS)
        ycor = random.choice(FOOD_POS)
        return xcor, ycor

    def spawn(self, cords):
        self.food.setpos(cords)
        self.food.dot()
