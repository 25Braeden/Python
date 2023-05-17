import turtle
x = turtle.Turtle()
y = turtle.Screen()
x.color('red', 'yellow')
while True:
    x.forward(100)
    x.left(77)
    if abs(x.pos()) < 1:
        break
y.exitonclick()