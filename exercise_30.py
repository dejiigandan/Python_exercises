import random

myfile = open("sowpods.txt", "r")


mylist = myfile.readlines()

a = random.choice(mylist)
b = random.choice(mylist)
print(a,b)

myfile.close()