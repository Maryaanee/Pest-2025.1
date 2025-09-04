notas = [0, 0, 0, 0]
tamLista = 4
print(notas)
# leia as notas e modifique a lista
# nota 1: 10. nota 2: 8.8. nota 3: 7.5. nota 4: 9.

notas[0] = 10.0
notas[1] = 8.8
notas[2] = 7.5
notas[3] = 9.0
print(notas)

# de maneira mais simples, usando for
for i in range(tamLista):
    notas[i] = float(input(f"Digite a nota {i+1}: "))

print(notas)

# calculo da media
media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
print(f"A média é: {media}")

# calculo da media de maneira mais simples, usando for
soma = 0
for i in range(tamLista):
    soma += notas[i]
    media2 = soma / tamLista
print(f"A média é for: {media2}")
