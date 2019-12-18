import random

a = str(random.sample(range(1000, 9999), 1))
print(a)

counter = 0
bulls = 0
user_num = input("Enter a 4-digit number: ")

if user_num[0] == a[1]:
    counter = counter + 1
elif user_num[0] in a:
    bulls = (bulls + 1)

if user_num[1] == a[2]:
    counter = counter + 1
elif user_num[1] in a:
    bulls = (bulls + 1)


if user_num[2] == a[3]:
    counter = counter + 1
elif user_num[2] in a:
    bulls = (bulls + 1)

if user_num[3] == a[4]:
    counter = counter + 1
elif user_num[3] in a:
    bulls = (bulls + 1)

print(f"{counter} cows, {bulls} bulls")


