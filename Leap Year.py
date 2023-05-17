a = int(input('What Year? '))
if (a % 100) == 0 & (a % 400) != 0:
    print('The year ',a,' is not a leap year.')
elif (a % 100) == 0 & (a % 400) == 0:
    print('The year ',a,' is a leap year.')
elif (a % 4) == 0:
    print('The year ',a,' is a leap year.')
else:
    print('The year ',a,' is not a leap year.)')