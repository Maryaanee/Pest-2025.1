num = int(input("Digite um número de 3 dígitos: "))
num2 = num

n1 = num // 100
n3 = num % 10

if n1 == n3:
    print(f"{num2} É um palíndromo.")
else:
    print("Não é um palíndromo.")