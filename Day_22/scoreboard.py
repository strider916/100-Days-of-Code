from turtle import Turtle
FONT = ("Arial", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write(self.l_score, align="center", font=FONT)
        

    def score_divider(self):
        divider = Turtle(shape="square")
        divider.shapesize(stretch_len=.1, stretch_wid=2)
        divider.color("white")
        divider.pu()
        divider.goto(0, 245)


