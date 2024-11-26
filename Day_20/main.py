from snake import Snake
from turtle import Screen
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
food = Food()
game_is_on = True
food_available = False
while game_is_on:
    food_cord = food.rand_pos()
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.segments[0].pos() == food.food.pos():
        snake.eat()
        food.food.clear()
        food_available = False

    if not food_available:
        food.spawn(food_cord)
        food_available = True


screen.exitonclick()
