#Robin Paranilam
#Turtle Polygons

import turtle

shapecolor = input("What color do you want the shape to be")
sidelength = int(input("How long do you want each side to be"))
polygonshape = int(input("How many sides do you want"))
n = (180 - (((polygonshape - 2)*180)/polygonshape))

wn = turtle.Screen()
wn.bgcolor(input("Enter your screen color"))
andy = turtle.Turtle()
andy.shape('turtle')
andy.color(shapecolor)

for x in range (0, polygonshape):
    andy.forward(sidelength)
    andy.right(n)
wn.exitonclick()








