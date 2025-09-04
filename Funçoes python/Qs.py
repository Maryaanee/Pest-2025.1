def soma(a : float, b : float):
    msoma = a + b
    print(f'A soma de {a} + {b} = {msoma}')

soma(1, 2)
soma(3, 5)
soma(10, 20)

def subtracao(a : float, b : float):
    msub = a - b
    return msub

aux = subtracao(1, 2)
print(f'A subtração de 1 - 2 = {aux}')
aux = subtracao(3, 5)
print(f'A subtração de 3 - 5 = {aux}')
