n = int(input("Digite um número: "))
n = n + 1
soma = 0
for i in range(0, n, 2):
    print(i)
    soma = soma + i
print(f"A soma foi: {soma}")