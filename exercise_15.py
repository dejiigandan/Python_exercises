
user_string = input("Enter your string here: ")


y = user_string.split()         #splits a string into a list
print(y)
print(" ".join(y[::-1]))        #[::-1] uses start of length-1 (default), an end of -1 (default), and step of -1. It is used to reverse a list