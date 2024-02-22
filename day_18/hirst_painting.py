import random

import colorgram
import turtle as t
import random


# def print_colors(colors):
#     lst_of_tuples = []
#     for color in colors:
#         rgb = tuple(color.rgb[i] for i in range(3))
#         lst_of_tuples.append(rgb)
#     print(lst_of_tuples)
#
#
# colors = colorgram.extract('image.jpg', 10)
# print_colors(colors=colors)


def make_row(turtle: t.Turtle, dots_amount, dot_size, margin, colors):
    for i in range(dots_amount):
        color = random.choice(colors)
        turtle.color(color)
        turtle.dot(dot_size)
        curr_x, curr_y = turtle.xcor(), turtle.ycor()
        turtle.goto(curr_x + margin, curr_y)


def draw_board(turtle: t.Turtle, dots_amount, rows_amount, dot_size, margin, colors):
    start_x = turtle.xcor()
    for _ in range(rows_amount):
        make_row(turtle=turtle,
                 dots_amount=dots_amount,
                 dot_size=dot_size,
                 margin=margin,
                 colors=colors)
        curr_y = turtle.ycor()
        turtle.goto(start_x, curr_y + margin)


color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
              (122, 175, 156), (229, 236, 239)]
tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.up()
tim.hideturtle()
tim.goto(-225, -225)
# print(tim.xcor())

draw_board(turtle=tim,
           dots_amount=10,
           dot_size=20,
           rows_amount=10,
           margin=50,
           colors=color_list)

screen = t.Screen()
screen.exitonclick()
