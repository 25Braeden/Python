from random import randint

x = randint(1, 3)
def RPS(inp):
    if len(inp) == 4:
        y = 1
    elif len(inp) == 5:
        y = 2
    elif len(inp) == 8:
        y = 3
    elif len(inp) != 4 or len(inp)!= 5 or len(inp) != 8:
        print("I didn't get that. Try again.")
        main()
    return y
def RPS2(x):
    if x == 1:
        print('The computer picked rock.')
    elif x == 2:
        print('The computer picked paper.')
    elif x == 3:
        print('The computer picked scissors.')

def RPS3(x, y):
    if (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
        print('You Win!')
    elif (x == 2 and y == 1) or (x == 3 and y == 2) or (x == 1 and y == 3):
        print('You Lose.')
    elif x == y:
        print("It's a tie! Try again.")

def main():
    y = RPS(input('Rock, Paper, or Scissors? '))
    RPS2(x)
    RPS3(x, y)

main()