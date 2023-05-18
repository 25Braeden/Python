import random

tries = 0
wins = 0
losses = 0
while tries <= 10000:

    dice1 = random.randint(1, 12)
if dice1 == 11 or dice1 == 7:
    if dice1 == 11:
        print("You rolled an 11; you win!!")
        wins += 1
        tries += 1
    elif dice1 == 7:
        print("You rolled a 7; you win!!")
        wins += 1
        tries += 1
elif dice1 == 2 or dice1 == 3 or dice1 == 12:
    if dice1 == 2:
        print("Your rolled a 2; you lose!!")
        losses += 1
        tries += 1
    elif dice1 == 3:
        print("You rolled a 3; you lose!!")
        losses += 1
        tries += 1
    elif dice1 == 12:
        print("You rolled a 12; you lose!!")
        losses += 1
        tries += 1
elif dice1 == 4 or dice1 == 5 or dice1 == 6 or dice1 == 8 or dice1 == 9 or dice1 == 10:
    k = 0
while k == 0:
    dice2 = random.randint(1, 12)
if dice2 == dice1:
    print("You rolled the point! You won!")
    wins += 1
    tries += 1
    k = 1
elif dice2 == 7:
    print("You rolled a 7 after the point! You lose!")
    tries += 1
    losses += 1
    k = 1

p = (wins / 10000) * 100
print("Your winning percentage is " + p + "%")

