
import random

chosen = int(input("Enter which number you want to bet on "))
bet = int(input("Place your bet amount: $"))
random1 = random.randint(1,38)
a = 1
money = 1000
while a == 1:
    if 1 <= chosen <= 38 and chosen == random1:
        money = (35 * bet + bet) + money
        print("You made 36 times your bet")
        break
    elif chosen == 39 and random1 <= 12:
        money = (bet + 2 * bet)+ money
        print("You made 3 times your bet")
        break
    elif chosen == 40 and 13 <= random1 <= 24:
        money = (bet + 2 * bet) + money
        print("You made 3 times your bet")
        break
    elif chosen == 41 and 25 <= random1 <= 36:
        money = (bet + 2 * bet) + money
        print("You made 3 times your bet")
        break
    elif chosen == 42 and random1 <= 18:
        money = 2 * bet + money
        print("You made 2 times your bet")
        break
    elif chosen == 43 and random1%2 == 0:
        money = 2 * bet + money
        print("You made 2 times your bet")
        break
    elif chosen == 46 and random1%2 != 0:
        money = 2 * bet + money
        print("You made 2 times your bet")
        break
    elif chosen == 47 and 19 <= random1 <= 36:
        money = 2 * bet + money
        print("You made 2 times your bet")
        break
    elif chosen == 44:
        if random1 == 1 or random1 == 3 or random1 == 5 or random1 == 7 or random1 == 9 or random1 == 12 or random1 == 14 or random1 == 16 or random1 == 18 or random1 == 19 or random1 == 21 or random1 == 23 or random1 == 25 or random1 == 27 or random1 == 30 or random1 == 32 or random1 == 34 or random1 == 36:
           money = (2 * bet) + money
           print("You made 2 times your bet")
           break
        else:
            money = money - bet
            print("The odds were not in your favor")
            break
    elif chosen == 45:
        if random1 == 2 or random1 == 4 or random1 == 6 or random1 == 8 or random1 == 10 or random1 == 11 or random1 == 13 or random1 == 15 or random1 == 17 or random1 == 20 or random1 == 22 or random1 == 24 or random1 == 26 or random1 == 28 or random1 == 29 or random1 == 31 or random1 == 33 or random1 == 35:
            money = (2 * bet) + money
            print("You made 2 times your bet")
            break
        else:
            money = money - bet
            print("The odds were not in your favor")
            break
    else:
        money = money - bet
        print("The odds were not in your favor")
        break
print("Your total is: $",money)