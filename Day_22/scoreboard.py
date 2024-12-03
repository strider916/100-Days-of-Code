from turtle import Turtle
FONT = ("Arial", 22, "normal")
GO_FONT = ("Script", 30, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(x=0, y=260)

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}   |   {self.r_score}", align="center", font=FONT)

    def game_over(self):
        # self.clear()
        self.goto(x=0, y=0)
        self.write("GAME OVER!", align="center", font=GO_FONT)
