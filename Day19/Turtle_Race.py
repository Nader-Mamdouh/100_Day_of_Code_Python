from turtle import Turtle, Screen
import random
is_race = False
screen = Screen()
screen.setup(width=500,height=400)
position = [-100, -50, 0, 50, 100]
colors = ["red", "orange", "yellow", "green", "blue"]
user_choice = screen.textinput(title="make your bet", prompt="Which turtle will win the race ? ")
all_turtles = []
for index in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-240, y=position[index])
    tim.color(colors[index])
    all_turtles.append(tim)
if user_choice:
    is_race = True
while is_race:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_choice:
                print("your turtle win the race :) ")
            else:
                print("you lose , the winner turtle is the "+winning_turtle)
            is_race = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
