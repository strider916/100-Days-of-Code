from turtle import Turtle
FONT = ("Courier", 6, "normal")


class StateNames(Turtle):
    def __init__(self, state, xy):
        super().__init__()
        self.color("Black")
        self.pu()
        self.ht()
        self.goto(xy)
        self.write(state, align="center", font=FONT)
