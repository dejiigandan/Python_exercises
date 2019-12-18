
lista = [1, 7, 9, 5, 3, 4, 4, 2, 9]
b = []
for e in lista:
    if e not in b:
        b.append(e)
print(b)



c = set(lista)
print(c)