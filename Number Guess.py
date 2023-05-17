from random import randint
z = '123'
while len(z) != 2:
    x = randint(1, 100)
    y = 0
    while x != y:
        y = input("What's your guess? ")
        y = int(y)
        if y < x:
            print('Too Small. Try Again.')
        if y > x:
            print('Too Big. Try Again')
    print('Correct!')
    z = input('Play Again? ')