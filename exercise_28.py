a = int(input("number 1: "))
b = int(input("number 2: "))
c = int(input("number 3: "))


if a > b and a > c:
    print(f"{a} is the greatest")
if b > a and b > c:
    print(f"{b} is the greatest")
if c > a and c > b:
    print(f"{c} is the greatest")