from turtle import Turtle
PADDLE_POS = [(-383, 0), (377, 0)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=4, stretch_len=.5)
        self.goto(position)

    def up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -260:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
