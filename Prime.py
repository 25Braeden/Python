x = int(input('What number? '))
n = 2 #counter
if x >= 2:
    while n < x:
        if x % n == 0:
            print('The number is not prime.')
            break
        elif x % n != 0:
            n += 1
        if n == x:
            print('The number is prime.')
if x < 2:
    print('Invalid number.')