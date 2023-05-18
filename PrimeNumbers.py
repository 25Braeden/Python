#Robin Paranilam

def get_integer():
   return int(input("Give me a number and I shall tell you if it's prime or not: "))




choice = get_integer()

if choice != 2 and choice != 3 and choice != 1 and choice != 5 and choice != 7 and (choice % 2 == 0 or  choice % 3 == 0 or choice % 7 == 0 or choice % 5 == 0):
    print("This number is composite")

else:
    print("This number is prime")
