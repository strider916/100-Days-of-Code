from snake import Snake
from listener import Listener
import time


s = Listener()

snake = Snake()
s.listen()


game_is_on = True
while game_is_on:
    s.update()
    time.sleep(.1)
    snake.move()

s.listen()
