from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.food = Turtle(shape="circle")
        self.food.color("aquamarine")
        self.food.pensize(10)
        self.food.pu()

    def randompos(self):
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        return xcor, ycor

    def spawn(self):
        self.food.setpos()
