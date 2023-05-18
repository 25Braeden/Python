#Robin Paranilam

print ('Enter a number and Lor Redox shall determine if it is a leap year')
year = int(input())
if (year%4 == 0 or year%400 == 0):
    print ('This year is a leap year!')

 if (year%4 == 0 and year%100 == 0):
    print ('This year is not a leap year!')

else:
    print ('This year is not a leap year!')