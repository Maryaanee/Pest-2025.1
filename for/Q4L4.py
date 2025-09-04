n = int(input("Digite um número: "))
n = n + 1
soma = 0
media = 0
for i in range(0, n, 1):
    print(i)
    media = media + 1
    soma = soma + i

print(f"A média foi: {soma // media} ")
print(f"calculo: {soma} / {media}")