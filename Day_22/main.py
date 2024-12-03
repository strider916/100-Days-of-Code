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
s = Scoreboard()
screen.listen()
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    s.update_score()
    # Check for winner
    if s.l_score == 3 or s.r_score == 3:
        ball.reset()
        s.game_over()
        game_on = False
    else:
        screen.update()

    ball.move()
    # Detect user controls
    screen.onkey(key="Up", fun=r_paddle.up)
    screen.onkey(key="Down", fun=r_paddle.down)
    screen.onkey(key="w", fun=l_paddle.up)
    screen.onkey(key="s", fun=l_paddle.down)

    # Detect top/bottom collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        ball.move_speed *= .95
    # Detect right wall collision
    if ball.xcor() > 380:
        ball.reset_position()
        s.l_score += 1
        ball.move()
    # Detect left wall collision
    if ball.xcor() < -380:
        ball.reset_position()
        s.r_score += 1
        ball.move()

screen.exitonclick()
