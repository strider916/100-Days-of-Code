import turtle
import pandas
from game_state import StateNames as St


screen = turtle.Screen()
screen.title(f'Correct States: {states_correct}/50')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=700, height=500)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_correct = 0
game_on = True

while states_correct < 50 and game_on:
    screen.title(f'States Correct: {states_correct}/50')
    screen.update()
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        state_loc = (state_data.x.item(), state_data.y.item())
        St(answer_state, state_loc)
        states_correct += 1
    elif answer_state == "exit".title():
        game_on = False
        break
