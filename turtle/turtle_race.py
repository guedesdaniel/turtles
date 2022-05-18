from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win this race? Choose the color: ")

colors = ['red', 'blue', 'orange', 'pink', 'green', 'purple']
turtles = []


for turtles_index in range(0, 6):
    turtle = Turtle(shape='turtle')
    turtle.penup()
    turtle.speed("fastest")
    turtle.color(colors[turtles_index])
    turtle.goto(x = -230, y = -80+30*turtles_index)
    turtles.append(turtle)

if user_bet:
    race_on = True


text = Turtle()
text.penup()
text.hideturtle()
text.goto(0, 170)
text.write(f"Your bet: {user_bet.lower()}", align='center', font=('Verdana', 15, "normal"))
#Turtle object to tell the winner on the screen
win_text = Turtle()
win_text.penup()
win_text.hideturtle()
win_text.goto(0, 120)

while race_on:
    for each_turtle in turtles:
        number = random.randint(0, 10)
        each_turtle.fd(number)
        if each_turtle.xcor() > 230:
            race_on = False
            winner = each_turtle.pencolor()
            if winner == user_bet.lower():
                win_text.write(f"You won the bet, CONGRATS! The {winner} turtle is the winner!!", align = 'center', font=('Verdana', 14, "normal"))
            else:
                win_text.write(f"You lost the bet!\nThe {winner} turtle is the winner!!", align = 'center', font=('Verdana', 10, "normal"))
            break



screen.exitonclick()