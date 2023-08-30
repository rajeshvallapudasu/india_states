import turtle
import random
import pandas
screen=turtle.Screen()

screen.title("My Indian States game")
image="rajeshindia.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
states_list=data["state"].to_list()
guessed_states=[]


while len(guessed_states)<36:
    answer_input = screen.textinput(title=f"{len(guessed_states)}/28 of total states",
                                    prompt=f"where's  the {random.choice(states_list)} state").title()
    if answer_input in states_list:
        guessed_states.append(answer_input)
        state=data[data["state"]==answer_input]
        t = turtle.Turtle()
        t.penup()
        t.goto(int(state.x),int(state.y))
        t.hideturtle()
        t.write(answer_input,font=("ariel",10,"bold"))
    if answer_input=="Exit":
        missed_states=[state for state in states_list if state not in guessed_states]

        pandas.DataFrame(missed_states).to_csv("missed_states.csv")

        break





