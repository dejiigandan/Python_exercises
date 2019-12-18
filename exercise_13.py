
q = int(input("How many numbers do you want: "))

def fibonacci():
    n=1
    if q ==1:
        print("[1]")
    elif q ==2:
        print("[1,1]")
    elif q > 2:
        mylist = [1, 1]
        while n < (q-1):
            mylist.append(mylist[n] + mylist[n-1])
            n+=1
    return mylist
print(fibonacci())