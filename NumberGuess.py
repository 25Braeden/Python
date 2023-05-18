#Robin Paranilam
import random

username = input("Enter your name ")
print (username,", I the great Robotron 3000 have found a number between 0 and 100. If you guess this number, I shall bestow upon you my riches. If you fail, then you will die. The choice is yours...")
y = random.randint(0, 100)

while True:
    guess = int(input("Enter your guess"))
    if guess > y:
        print("Your guess is too high young padawan")

    elif guess < y:
        print("Your guess is too low young padawan")

    elif guess == y:
        print("You're a genius!! I shall bestow upon you my gifts,",username,"!")
        break
