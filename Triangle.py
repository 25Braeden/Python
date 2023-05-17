import math
import turtle

typ = input('Do you need the leg or the hypotenuse? ')
if len(typ) == 10:
    a = float(input('What is the length of side a? '))
    b = float(input('What is the length of side b? '))
    c = math.sqrt((a**2) + (b**2))
    print('The hypotenuse is', c)
if len(typ) == 3:
    a = float(input('What is the length of side a? '))
    c = float(input('What is the length of side c? '))
    b = math.sqrt((c**2) - (a**2))
    print('The other leg is', b)

wn = turtle.Screen()
t = turtle.Turtle()
t.color('blue')
print(a)
print(b)
print(c)
t.goto(-100, 40)
A = math.sin(a/c)
B = math.sin(b/c)
t.forward(a)
t.left(90)
t.forward(b)
t.left(180 - A)
t.forward(c)
#wn.exitonelick()