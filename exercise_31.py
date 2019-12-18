import random

myfile = open("sowpods.txt", "r")


mylist = myfile.readlines()

a = random.choice(mylist)
print(a)

myfile.close()

for e in a:
    print(e)

