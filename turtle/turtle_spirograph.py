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


dan.speed("fastest")
dan.color(random_color())
dan.pensize(1)

def draw_spirograph(circles): # circles number of circles you want to be draw
    angle = 360/circles  #
    for _ in range(circles):
        dan.circle(100)
        dan.seth(dan.heading() + angle)
        dan.color(random_color())


draw_spirograph(100)

screen = t.Screen()
screen.exitonclick()



