              # 1.  import the modules
import random
import turtle
from random import randint
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
ab = turtle.Turtle()
ac = turtle.Turtle()
ad = turtle.Turtle()
ae = turtle.Turtle()
lance.color('red')
andy.color('blue')
ab.color('purple')
ac.color('yellow')
ad.color('orange')
ae.color('rainbow')
lance.shape('turtle')
andy.shape('turtle')
ab.shape('turtle')
ac.shape('turtle')
ad.shape('turtle')
ae.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
ab.up()
ac.up()
ad.up()
ae.up()
lance.up()
andy.goto(-100,20)
ab.goto(-100, 40)
ac.goto(-100, -40)
ad.goto(-100, 60)
ae.goto(-100, -60)
lance.goto(-100,-20)

x = 0
while x < 10:
    q = randint(1, 2)
    w = randint(1, 2)
    andy.forward(80)
    lance.forward(80)
    ab.forward(80)
    ac.forward(80)
    ad.forward(80)
    ae.forward(80)
    if q == 1:
        andy.left(randint(0, 180))
    if q == 2:
        andy.right(randint(0, 180))
    if w == 1:
        lance.left(randint(0, 180))
    if w == 2:
        lance.right(randint(0, 180))
    if q == 1:
        ab.left(randint(0, 180))
    if q == 2:
        ab.right(randint(0, 180))
    if q == 1:
        ac.left(randint(0, 180))
    if q == 2:
        ac.right(randint(0, 180))
    if q == 1:
        ad.left(randint(0, 180))
    if q == 2:
        ad.right(randint(0, 180))
    if q == 1:
        ae.left(randint(0, 180))
    if q == 2:
        ae.right(randint(0, 180))
    andy.forward(randint(0, 25))
    lance.forward(randint(0, 25))
    ab.forward(randint(0, 25))
    ac.forward(randint(0, 25))
    ad.forward(randint(0, 25))
    ae.forward(randint(0, 25))
    x = x + 1

wn.exitonclick()
