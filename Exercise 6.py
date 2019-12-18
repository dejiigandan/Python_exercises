word = input("Try your word here: ")
a = list(word)
b=a.copy()
b.reverse()

if a == b:
    print("Yes! This word is a palindrome")
else:
    print("This is not a palindrome")