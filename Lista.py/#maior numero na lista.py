#maior numero na lista



def maior_numero(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

lista = [1, 10, -3, 40, 35, 78, -110, 0]
val = maior_numero(lista)

print(f'O maior número da lista é: {val}')