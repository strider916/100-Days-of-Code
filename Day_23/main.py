import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()
cars = CarManager()
speed_multiplier = 0.1

screen.listen()
screen.onkey(key="Up", fun=player.go_up)

game_is_on = True
while game_is_on:

    for _ in range(6):
        time.sleep(speed_multiplier)
        screen.update()
        cars.move_cars()
        cars.destroy()
        if player.check_win():
            player.check_win()
            score.level += 1
            score.update_level()
            speed_multiplier *= .9
        for car in cars.all_cars:
            if player.distance(car) <= 20:
                score.goto(0, 0)
                score.game_over()
                game_is_on = False
    cars.create_car(300, random.randint(-250, 250), 1)


screen.exitonclick()
