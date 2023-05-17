import turtle
import random
from random import randint
wn = turtle.Screen()
wn.bgcolor('lightblue')

lance = turtle.Turtle()
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

x = randint(-250, 200)
andy.up()
lance.up()
andy.goto(-300,0)
lance.goto(x, 0)

y = -300
z = randint(1, 2)

while y < x - 40:
    andy.forward(1)
    y = y + 1
if z == 1:
    andy.right(90)
    andy.forward(40)
    andy.left(90)
    andy.forward(80)
    andy.left(90)
    andy.forward(40)
    andy.right(90)
    andy.forward(300 - x)
elif z == 2:
    andy.left(90)
    andy.forward(40)
    andy.right(90)
    andy.forward(80)
    andy.right(90)
    andy.forward(40)
    andy.left(90)
    andy.forward(300 - x)

wn.exitonclick()