"""
    參考網頁:
        http://yltang.net/tutorial/python/5/
        https://docs.python.org/zh-tw/3/library/turtle.html#turtle.pd
"""
import math
from turtle import Turtle, Screen

screen = Screen()
screen.setworldcoordinates(0, 0, 100, 100)

emily = Turtle(visible=False)
emily.speed(0)
emily.forward(100)
emily.forward(-100)
emily.left(90)
emily.forward(100)
emily.penup()


def straight_line_ud(x, num1, num2):
    for y in range(num1, num2 + 1):  # logn
        emily.goto(x, y)
        emily.pendown()
    emily.penup()


def straight_line_lr(y, num1, num2):
    for x in range(num1, num2 + 1):  # logn
        emily.goto(x, y)
        emily.pendown()
    emily.penup()


def char_n(x_min, y_min):
    straight_line_ud(x_min, y_min, y_min + 3)
    straight_line_lr(y_min + 2, x_min, x_min + 1)
    straight_line_ud(x_min + 1, y_min, y_min + 2)


def char_2(x_min, y_min):
    straight_line_lr(y_min, x_min, x_min + 1)
    straight_line_ud(x_min + 1, y_min, y_min + 1)
    straight_line_lr(y_min + 1, x_min, x_min + 1)
    straight_line_ud(x_min + 1, y_min + 1, y_min + 2)
    straight_line_lr(y_min + 2, x_min, x_min + 1)


def char_3(x_min, y_min):
    straight_line_lr(y_min, x_min, x_min + 1)
    straight_line_ud(x_min, y_min, y_min + 1)
    straight_line_lr(y_min + 1, x_min, x_min + 1)
    straight_line_ud(x_min + 1, y_min + 1, y_min + 2)
    straight_line_lr(y_min + 2, x_min, x_min + 1)


def char_l(x_min, y_min):
    straight_line_ud(x_min, y_min, y_min + 4)


def char_o(x_min, y_min):
    straight_line_ud(x_min, y_min, y_min + 2)
    straight_line_lr(y_min, x_min, x_min + 1)
    straight_line_ud(x_min + 1, y_min, y_min + 2)
    straight_line_lr(y_min + 2, x_min, x_min + 1)


def char_g(x_min, y_min):
    straight_line_ud(x_min, y_min + 3, y_min + 4)
    straight_line_lr(y_min + 4, x_min, x_min + 1)
    straight_line_ud(x_min + 1, y_min, y_min + 4)
    straight_line_lr(y_min + 3, x_min, x_min + 1)
    straight_line_lr(y_min, x_min, x_min + 1)


emily.penup()
for x in range(1, 101):  # logn
    y = math.log(x)
    emily.goto(x, y)
    emily.pendown()

emily.penup()

# logn
char_l(87, 8)
char_o(88, 8)
char_g(90, 6)
char_n(92, 8)

for x in range(0, 101):  # n
    y = x
    emily.goto(x, y)
    emily.pendown()

emily.penup()

# n
char_n(85, 87)

for x in range(1, 101):  # nlogn
    y = x * math.log(x)
    emily.goto(x, y)
    emily.pendown()
    if y >= 100:
        break

emily.penup()

# nlogn
char_n(17, 87)
char_l(19, 87)
char_o(20, 87)
char_g(22, 85)
char_n(24, 87)

for x in range(0, 101):  # n ^ 2
    y = x ** 2
    emily.goto(x, y)
    emily.pendown()
    if y >= 100:
        break

emily.penup()

# n^2
char_n(7, 87)
char_3(8, 90)

for x in range(0, 101):  # n ^ 3
    y = x ** 3
    emily.goto(x, y)
    emily.pendown()
    if y >= 100:
        break

emily.penup()

# n^3
char_n(2, 87)
char_2(3, 90)

screen.exitonclick()
