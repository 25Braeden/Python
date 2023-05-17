from random import randint
x = [30, 6, 53, 82, 54, 15, 74, 3, 67, 38]
print(x)
z = 0
while z <= 9:
    if x[z] < 10:
        print(z)
        del x[z]
        z = z - 1
    z = z + 1
print(x)
