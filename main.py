from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "grey", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet.", prompt=f"Which turtle will win teh race? {colors}: ")
turtles = []


def make_turtle():
    quantity = len(colors)
    ini_x = -230
    ini_y = -100
    for _ in range(quantity):
        turtle_color = colors[_]
        turtles.append(Turtle(shape="turtle"))
        turtles[_].color(turtle_color)
        turtles[_].penup()
        turtles[_].goto(ini_x, ini_y)
        ini_y += 40
    return turtles


def run_turtle():
    while True:
        for turtle in turtles:
            dist = random.randint(1, 5)
            turtle.forward(dist)
            pos_x = turtle.xcor()
            if pos_x >= 220:
                return turtle.color()[0]


make_turtle()
winner = run_turtle()
if winner == user_bet:
    print(f"You won, {winner} was first")
else:
    print(f"You lost, {winner} was first")
screen.exitonclick()