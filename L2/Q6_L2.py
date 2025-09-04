n = int(input("Digite um número de 5 dígitos: "))

d1 = n % 10
n = n // 10

d2 = n % 10
n = n // 10

d3 = n % 10
n = n // 10


d4 = n % 10
n = n // 10

d5 = n % 10

if (d1 == d2) or (d1 == d3) or (d1 == d4) or (d1 == d5):
    print("Digito 1 se repete")
if (d2 == d3) or (d2 == d4) or (d2 == d5):
    print("Digito 2 se repete")
if (d3 == d4) or (d3 == d5):
    print("Digito 3 se repete")
if (d4 == d5):
    print("Digito 4 se repete")




