from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    score.update_scoreboard()
    screen.update()
    time.sleep(.1)
    snake.move()

    for seg in range(2, len(snake.segments) - 1):
        if snake.head.distance(snake.segments[seg]) < 5:
            score.game_over()
            game_is_on = False
    if snake.head.distance(food) < 15:
        snake.eat()
        food.refresh()
        score.add_point()
    if snake.head.ycor() >= 300 or snake.head.ycor() <= -300 or snake.head.xcor() >= 300 or snake.head.xcor() <= -300:
        score.game_over()
        game_is_on = False


screen.exitonclick()
