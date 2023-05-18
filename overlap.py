import random

first_list= random.sample(range(15),8)

second_list=random.sample(range(20),11)

print (first_list)

print (second_list)

common_numbers= []

for num in first_list:

    if num in second_list:
        common_numbers.append(num)

print (common_numbers)
print (common_numbers.sort)
