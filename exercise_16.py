
import random

# a = random.sample(range(1, 99), 2)
# e = random.sample(("a","c","d","e","j","i","l","H","Y","N","E","G","Q","X"), 5)
# print(a)
# " ".join(e)
# print(e)
#
#
# mylist = []
# for i in a:
#     mylist.append(i)
#
# for i in e:
#     mylist.append(e)
# print(mylist)

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"



p =  "".join(random.sample(s, 16))

print (p)