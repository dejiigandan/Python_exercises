


num = int(input("Please state a number: "))
if num % 4 == 0:
    print("This number is divisible by 4")
elif num%2 == 0:
    print("This is an even number")
else:
    print("This is not an even number")

num = int(input("Input number here: "))
check = int(input("Input another number: "))
if num%check == 0:
    print(str(num) + ' is divisible by ' + str(check))
else:
    print(str(num) + ' is not divisible by ' + str(check))