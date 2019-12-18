a = open("primenums", "r")
ar = a.read()
b = open("happynums", "r")
br = b.read()

print(ar)
alist = []


for num in ar:
    if num in br:
        alist.append(num)
a.close("primenums")
b.close("happynums")