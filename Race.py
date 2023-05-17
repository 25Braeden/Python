import turtle
from random import randint
Lance = turtle.Turtle()
Ralph = turtle.Turtle()
pen = turtle.Turtle()
scn = turtle.Screen()

pen.penup()
pen.goto(300, 40)
pen.pendown()
pen.goto(300, -40)
pen.penup()

Lance.color('red')
Lance.shape('turtle')
Ralph.color('blue')
Ralph.shape('turtle')
Ralph.penup()
Lance.penup()
Lance.goto(-200, 20)
Ralph.goto(-200, -20)

while int(Lance.xcor()) < 300 & int(Ralph.xcor()) < 300:
    Lance.forward(int(randint(0, 10)))
    Ralph.forward(int(randint(0, 10)))

    # scn.exitonclick()
if Lance.xcor() >= 300:
    print('Lance Wins')
if Ralph.xcor() >= 300:
    print('Ralph Wins')
print(Lance.xcor())
print(Ralph.xcor())
scn.exitonclick()