mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num2 = 88


def takenum(arg1, arg2):
    if arg2 in arg1:
        return True
    else:
        return False

print(takenum(mylist, num2))

