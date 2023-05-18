#Robin Paranilam


import turtle
import random
wn = turtle.Screen()
racer = turtle.Turtle()
racer.speed(20)
racer.penup()
racer.goto(-140, 140)
for step in range(15):
    racer.write(step, align='center')
    racer.right(90)
    for num in range(8):
        racer.penup()
        racer.forward(10)
        racer.pendown()
        racer.forward(10)
    racer.penup()
    racer.backward(160)
    racer.left(90)
    racer.forward(20)

ada = turtle.Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(10):
    ada.right(36)

bob = turtle.Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(72):
    bob.left(5)

ivy = turtle.Turtle()
ivy.shape('turtle')
ivy.color('green')

ivy.penup()
ivy.goto(-160, 40)
ivy.pendown()

for turn in range(60):
    ivy.right(6)

jim = turtle.Turtle()
jim.shape('turtle')
jim.color('orange')

jim.penup()
jim.goto(-160, 10)
jim.pendown()

for turn in range(30):
    jim.left(12)

for turn in range(100):
    ada.forward(random.randrange(1, 5))
    bob.forward(random.randrange(1, 5))
    ivy.forward(random.randrange(1, 5))
    jim.forward(random.randrange(1, 5))

wn.exitonclick()
