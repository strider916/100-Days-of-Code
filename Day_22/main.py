from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


# Create each paddle object at the specified position
l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))

ball = Ball()

screen.listen()
game_on = True
while game_on:
    time.sleep(.02)
    s = Scoreboard()
    screen.update()
    ball.move()
    screen.onkey(key="Up", fun=r_paddle.up)
    screen.onkey(key="Down", fun=r_paddle.down)
    screen.onkey(key="w", fun=l_paddle.up)
    screen.onkey(key="s", fun=l_paddle.down)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        s.p1_score += 1
        ball.move()
    if ball.xcor() < -380:
        ball.reset_position()
        s.p2_score += 1
        ball.move()

screen.exitonclick()
