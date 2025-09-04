lista = [1, 2, "três", 4.5, 6.6, 10, -1, 0]

# imprima todos os elementos da lista com while
contador = 0
print("imprimindo com while")
while contador <= 7:
    print(lista[contador])
    contador += 1 

# imprima todos os elementos da lista com for
print("imprimindo com for")
for contador2 in range(8):
    print(lista[contador2])