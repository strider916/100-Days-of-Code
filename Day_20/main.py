from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
with open("data.txt", mode="r") as data:
    screen.title(f"Snake Game | High Score: {int(data.read())}")
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
    screen.title(f"Snake Game | High Score: {score.high_score}")
    score.update_scoreboard()
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_scoreboard()
            snake.reset_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        score.add_point()

    # Detect collision with wall
    if snake.head.ycor() >= 300 or snake.head.ycor() <= -300 or snake.head.xcor() >= 300 or snake.head.xcor() <= -300:
        score.reset_scoreboard()
        snake.reset_snake()


screen.exitonclick()
