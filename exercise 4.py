num = int(input("Please state your number: "))
a = range(1, int(num-1))
for e in a:
    if num%e == 0:
        print(e)