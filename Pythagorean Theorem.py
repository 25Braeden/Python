#RobinParanilam
import math
a = float(input("Enter the length of the first leg"))
b = float(input("Enter the length of the second leg"))

def hypotenuse(lega,legb):
    lega = a ** 2
    legb = b ** 2
    c = lega + legb
    legc = math.sqrt(c)
    return legc
side = hypotenuse(a,b)
print("The length of the hypotenuse is", side)








