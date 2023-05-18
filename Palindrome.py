#Robin Paranilam

s = input()
r = ""
for item in s:
    r = item.lower() + r

if r == s:
    print("It is a palindrome")

else:
    print("It is not a palindrome")


