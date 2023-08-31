import turtle
from turtle import Turtle, Screen
import random
import colorgram


# def random_color():
#     return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


gram_color_list = colorgram.extract('picture.jfif', 20)
rgb_color_list = []

for i in gram_color_list:
    r = i.rgb[0]
    g = i.rgb[1]
    b = i.rgb[2]
    if (220 < r < 255) and (220 < g < 255) and (220 < b < 255):
        pass
    else:
        new_color = (r, g, b)
        rgb_color_list.append(new_color)


timmy = Turtle()
turtle.colormode(255)
timmy.speed(0)

timmy.penup()
timmy.left(225)
timmy.forward(200)
timmy.right(225)

count = 1
for _ in range(10):
    for _ in range(9):
        timmy.dot(10, random.choice(rgb_color_list))
        timmy.forward(30)
    timmy.dot(10, random.choice(rgb_color_list))
    count += 1
    if count % 2 == 0:
        timmy.left(90)
        timmy.forward(30)
        timmy.left(90)
    else:
        timmy.right(90)
        timmy.forward(30)
        timmy.right(90)

timmy.hideturtle()
screen = Screen()
screen.exitonclick()
