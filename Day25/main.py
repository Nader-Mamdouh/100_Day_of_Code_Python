import turtle,pandas
screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 states correct",
                                    prompt="What is another state ?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_location = data[data.state == answer_state]
        t.goto(int(state_location.x), int(state_location.y))
        t.write(state_location.state.item())












screen.exitonclick()
