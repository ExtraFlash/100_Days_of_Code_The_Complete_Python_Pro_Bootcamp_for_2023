import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

done = False
score = 0

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()  # make each word capitalized
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # get row from data
        t.goto(int(state_data.x.item()), int(state_data.y.item()))  # item() gets the first scalar in a data structure
        print(type(state_data.x))
        t.write(state_data.state.item())

# while not done:
#     answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#     capitalized_words = [word.capitalize() for word in answer_state.split()]
#     capitalized_answer = ' '.join(capitalized_words)
#
#     if len(df[df.state == capitalized_answer]) == 0:
#         done = True
#     else:


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
