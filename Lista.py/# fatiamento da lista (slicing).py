# fatiamento da lista (slicing)
# lista[start:end:step]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
print(lista[0:5])  # [1, 2, 3, 4, 5]
print(lista[5:])  # [6, 7, 8, 9, 10]
print(lista[:5])  # [1, 2, 3, 4, 5]
print(lista[10:])  # [a, b, c, d, e]
print(lista[::2])  # [1, 3, 5, 7, 9, b, d]