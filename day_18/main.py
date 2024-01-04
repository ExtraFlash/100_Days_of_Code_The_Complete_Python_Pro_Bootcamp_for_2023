import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

colors = ['yellow', 'black', 'orange', 'pink', 'grey']
# tim.pensize(15)
tim.speed('fastest')

num_steps = 500


def random_color():
    r = random.choice(range(256))
    g = random.choice(range(256))
    b = random.choice(range(256))
    color = (r, g, b)
    return color


angle_speed = 4
for _ in range(360 // angle_speed):
    tim.color(random_color())
    tim.circle(radius=100)
    tim.right(angle_speed)

screen = t.Screen()
screen.exitonclick()
