
import random

a = random.choice(range(1, 10))

user_num = input("Enter your number here: ")
counter = 0

while user_num !="exit":
    counter = 1 + counter
    if int(user_num) == a:
        print("You guessed right")
        user_num = input("Enter your number here: ")
    if int(user_num) > a:
        print("Your value is too great")
        user_num = input("Enter your number here: ")
    if int(user_num) < a:
        print("Your value is too small")
        user_num = input("Enter your number here: ")

if user_num == "exit":
    print(counter)
    exit()


