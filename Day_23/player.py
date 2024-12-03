from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.speed("fastest")
        self.setheading(90)

    def move(self):
        new_y = (self.ycor() + MOVE_DISTANCE)
        self.goto(self.xcor(), new_y)

    def check_win(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
