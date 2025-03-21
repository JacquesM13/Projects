from turtle import Turtle, Screen
import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

FONT = ('Arial', 10, 'normal')

turtle = Turtle()
screen = Screen()

screen.title("U.S. States Game")
screen.setup(width= 725, height= 491)
image = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guessed = []

while len(guessed) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed)}/50 States Correct",
                                     prompt="What's another state name?")).title()
    if answer_state in states and answer_state not in guessed:
        guessed.append(answer_state)
        tag = Turtle()
        tag.penup()
        tag.hideturtle()
        state_data = data[data.state == answer_state]
        tag.goto(state_data.x.item(), state_data.y.item())
        tag.write(arg= f"{answer_state}", font= FONT)

    if answer_state == "Exit":
        states_to_learn = [state for state in states if state not in guessed]
        # for state in states:
        #     if state not in guessed:
        #         states_to_learn.append(state)
        states_to_learn_DF = pandas.DataFrame(states_to_learn)
        states_to_learn_DF.to_csv("states_to_learn.csv")
        break