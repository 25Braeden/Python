import math
import turtle

side = input('How many sides? ')

sc = turtle.Screen()
sc.bgcolor('white')

pen = turtle.Turtle()
pen.shape('arrow')
pen.pencolor = ()
pen.degrees(fullcircle = 360.0)
#pen.goto(-100, 40)

side = int(side)
aIAng = (side - 2) * 180
intAng = aIAng / side
extAng = 180 - intAng

x = 0

if side >= 3:
    while x < side:
        pen.forward((side * 1000) / (side ** 2))
        pen.left(extAng)
        x = x + 1

    sc.exitonclick()
