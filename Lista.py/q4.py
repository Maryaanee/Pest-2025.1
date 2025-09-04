lista = [1, 2, 3, 4, 5]
num = int(input("Digite um número: "))

for item in lista:
    if num == item:
        print('o numero digitado está na lista')
        item = 0
        print(f'a lista agora é: {lista}')
        break 
    else:
        print('A fruta digitada não está na lista')
