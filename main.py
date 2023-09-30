import turtle as t
import pandas as p

FONT = ("Arial", 12, "normal")

screen = t.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)

states_list = []
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"You've guessed {len(guessed_states)}/50", "'Nother one").title()
    states = p.read_csv("50_states.csv")
    if answer_state == 'Exit':
        break

    for s in states['state']:

        if answer_state == s:
            guessed_states.append(answer_state)
            state_data = (states[states['state'] == s])
            states_list.append(t.Turtle())
            states_list[-1].hideturtle()
            states_list[-1].color('black')
            states_list[-1].penup()
            cor_x = state_data.x.item()
            states_list[-1].goto(state_data.x.item(), state_data.y.item())
            states_list[-1].write(f"{state_data.state.item()}", align='center', font=FONT)
            break

states_to_learn = states.state.tolist()
for s in guessed_states:
    states_to_learn.remove(s)
csv_file = p.DataFrame(states_to_learn)
csv_file.to_csv("states_to_learn.csv")
