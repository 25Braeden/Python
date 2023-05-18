
import turtle
import random
jim = turtle.Turtle()
jim.shape('turtle')
jim.color('orange')
jim.penup()
jim.goto(-160, 10)
jim.pendown()
andy = turtle.Turtle()
andy.shape('turtle')
andy.color('green')
andy.penup()
andy.goto(100,10)
for turn in range(100):
    jim.forward(random.randint(1,5))
    if (jim.xcor() == 60):
        jim.left(90)
        jim.forward(25)
        jim.right(90)
        jim.forward(50)
wn = turtle.Screen()
wn.exitonclick()
