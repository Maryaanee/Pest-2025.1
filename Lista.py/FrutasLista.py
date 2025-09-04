#verifiquie se a fruta digitada está na lista de frutas

frutas = ['uva', 'banana', 'laranja', 'maçã', 'pera']

fruta = input('Digite o nome de uma fruta: ')

for item in frutas:
    if fruta == item:
        print('A fruta digitada está na lista')
    