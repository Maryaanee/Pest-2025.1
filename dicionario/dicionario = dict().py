dicionario = dict()

for i in range(5):
    chave = input(f"Digite a palavra chave {i+1}: ").lower()
    valor = input(f"Digite a definição para {chave}: ").lower()

while true:
    chave = input("Digite a chave ou zero para sair: ").lower()
    if chave == "0" or chave == "zero":
        break
    else:
        if chave in dicionario:
            print(dicionario[chave])
        else:
            print("chave inexistente")