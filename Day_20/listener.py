from turtle import Screen
import snake


class Listener:
    def __init__(self):
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)

    def listen(self):
        self.listen()
        self.onkey(key="Up", fun=snake.up)
        self.onkey(key="Down", fun=snake.down)
        self.onkey(key="Left", fun=snake.left)
        self.onkey(key="Right", fun=snake.right)