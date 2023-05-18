import random

y = random.randint(1,3)

choice = int(input("This is a rock paper scissors match between you and I, the great Robotron 3000;" + "\n" + "Choose: " + "\n" "1 for rock:" + "\n"  + "2 for paper:" + "\n" + "3 for scissors: "))


if choice == 1 and y == 2:
    print ("You have lost; The great Robotron 3000 wins again! I chose paper.")
elif choice == 1 and y == 3:
    print("Noo! I have been defeated and you have prevailed! I chose scissors.")
elif choice == 1 and y == 1:
    print("Wow! Our power levels are matched and we are tied in battle...I chose rock.")
elif choice == 3 and y == 1:
    print("You have lost; The great Robotron 3000 wins again! I chose rock.")
elif choice == 3 and y == 2:
    print("Noo! I have been defeated and you have prevailed! I chose paper.")
elif choice == 3 and y == 3:
    print("Wow! Our power levels are matched and we are tied in battle...I chose scissors.")
elif choice == 2 and y == 3:
    print("You have lost; The great Robotron 3000 wins again! I chose scissors.")
elif choice == 2 and y == 1:
    print("Noo! I have been defeated and you have prevailed! I chose rock.")
elif choice == 2 and y == 2:
    print("Wow! Our power levels are matched and we are tied in battle... I chose paper.")
