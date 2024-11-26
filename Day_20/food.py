from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.pu()
        self.color("aquamarine")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_x = random.randrange(-280, 280, 18)
        ran_y = random.randrange(-280, 280, 18)

        self.setpos(ran_x, ran_y)

