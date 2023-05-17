str = input('Palindrome Test: ').lower()
str = str.replace(' ', '').replace('.', '').replace('!', '').replace('?', '').replace(',', '').replace("'", '')
x = len(str) - 1
y = 0
while y <= x:
    if str[y] != str[x]:
        print('Not a Palindrome')
        break
    x = x - 1
    y = y + 1
if x < y:
    print("It's a Palindrome")