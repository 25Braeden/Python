import random
a = random.sample(range(31), 10)
b = random.sample(range(31), 10)
print(a)
print(b)
c = []
n = 0
while n < 9:
    if b[n] in a:
       # print('True')
        c.insert(n, b[n])
        n = n + 1
    else:
        #print('False')
        n = n + 1
print(c)