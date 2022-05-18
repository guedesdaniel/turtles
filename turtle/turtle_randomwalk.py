import turtle as t
import random

dan = t.Turtle()

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
dan.pensize(15)
dan.speed("fastest")

for _ in range(300):
    dan.color(random_color())
    dan.forward(random.randint(30,50))
    dan.seth(random.choice(directions))


screen = t.Screen()
screen.exitonclick()



