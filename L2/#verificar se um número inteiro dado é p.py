#verificar se um número inteiro dado é par ou ímpar.

numero = int(input("Digite um número: "))

pares = "não é impar, é par"
impar = "não é par, é impar"

if numero == 0:
    print("Zero é neutro, não é nem par nem ímpar.")
elif numero % 2 == 0:
    numero = pares
else:
    numero = impar

print(f"{numero}")
   