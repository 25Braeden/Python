file = open("nameslist.txt", "r")

counter1 = 0
counter2 = 0
counter3 = 0
for aline in file:
    values = aline.split()
    if values[0] == "Anakin":
        counter1 = counter1 + 1
    elif values[0] == "Luke":
        counter2 = counter2 + 1
    elif values[0] == "Leia":
        counter3 = counter3 + 1



file.close()
print("Anakin was printed", counter1, "times")
print("Luke was printed", counter2, "times")
print("Leia was printed", counter3, "times")