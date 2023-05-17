import turtle
Lance = turtle.Turtle()
Ralph = turtle.Turtle()
pen = turtle.Turtle()
scn = turtle.Screen()

pen.penup()
pen.goto (300, 40)
pen.pendown()
pen.goto (300, -40)
pen.penup()

Lance.color('red')
Lance.shape('turtle')
Ralph.color('blue')
Ralph.shape('turtle')
Ralph.penup()
Lance.penup()
Lance.goto(-300, 20)
Ralph.goto(-300, -20)

def btnPress('Left'):
Lance.onrelease(btn=102)

Ralph.onrelease(btn='A')

scn.exitonclick()
