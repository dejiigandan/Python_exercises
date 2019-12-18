f = open("text1.txt", "r")
counter = 0
for line in f:
    print(line)
    counter = counter + 1
print(counter)



student_scores = {'Adama': 100, 'Starbuck': 75, 'Apollo': 80, 'Athena': 85, 'Agathon': 90}

for pair in student_scores.items():
    print(pair)