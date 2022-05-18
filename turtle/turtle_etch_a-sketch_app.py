import turtle as t
import random

dan = t.Turtle()
t.colormode(255)

dan.color('blue')
dan.speed("fast")
dan.pensize(2)


def turn_right():
    dan.seth(dan.heading() - 10)


def turn_left():
    dan.seth(dan.heading() + 10)


def move_backwards():
    dan.bk(10)


def move_forwards():
    dan.fd(10)


def clear():
    dan.clear()
    dan.penup()
    dan.home()
    dan.seth(0)
    dan.pendown()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    dan.color(random_colors)


def circle():
    dan.circle(100)


def penup():
    dan.penup()


def pendown():
    dan.pendown()


screen = t.Screen()
text = t.Turtle()
text.penup()
text.hideturtle()
text.goto(0, 350)
text.write("C = clean / R = circle / G = change / U = pen up / D = pen down", align ='center', font=('Verdana', 15, "normal"))
screen.listen()
screen.onkeypress(move_forwards, "Up")
screen.onkeypress(move_backwards, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkey(random_color, "g")
screen.onkey(circle, "r")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(clear, "c")
screen.onkeypress(penup, "u")
screen.onkeypress(pendown, "d")
screen.exitonclick()





