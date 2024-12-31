import turtle
import tkinter
from game_state import StateNames


screen = turtle.Screen()
states_correct = 0
screen.title(f'Correct States: {states_correct}/50')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=700, height=500)
screen.tracer()
states = []
states_dict = []

with open("50_states.csv", "r") as csv:
    for line in csv:
        line = line.replace('\n', '')
        state_info = line.split(',')
        states.append(state_info)
keys = states.pop(0)

for values in states:
    this = dict(zip(keys, values))
    states_dict.append(this)


while states_correct < 50:
    screen.title(f'Correct States: {states_correct}/50')
    screen.update()
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    for d in states_dict:
        if d["state"] == answer_state:
            state_coords = (int(d["x"]), int(d["y"]))
            StateNames(d["state"], state_coords)
            states_correct += 1
            break

screen.mainloop()

