from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.ht()
        self.pu()
        self.goto(-230, 260)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.write(f"GAME OVER", align="center", font=FONT)
