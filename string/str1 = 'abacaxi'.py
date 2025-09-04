str1 = 'abacaxi'
str2 = 'MELANCIA'

print(str1[3])
print(str2[2:])

print(f"Tamanho da string 1: {len(str1)} caracteres")
print(f"Tamanho da string 2: {len(str2)} caracteres")

#percorrendo os elementos 

print(f"imprimir os elementos de {str1}")
for caractere in range(len(str1)):
    print(str1[caractere])