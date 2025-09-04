#Aluna: Francisca Mariane Sousa da Silva
#Aluno: José Hadriel Miranda dos Santos 
# Turma S3
# Data: 30/05/2025

# Função que exibe o menu de opções para o usuário
def menu():
    print("*~~*~~*~~   📚 MENU DE CONJUNTOS   *~~*~~*~~")
    print("[1] ➕ Criar Conjunto")
    print("[2] 🧮 Adicionar Elemento")
    print("[3] ➖ Remover Elemento")
    print("[4] 👀 Mostrar Conjuntos")
    print("[5] 🗑️ Apagar Conjunto")
    print("[6] ∪ União de Conjuntos")
    print("[7] ∩ Interseção de Conjuntos")
    print("[0] ❌ Sair\n")
    print("-" * 45)
    print("Escolha uma opção para continuar... 🔢")
    print("*~~" * 15)

# Listas para armazenar os nomes e os elementos dos conjuntos
lista_nomes = []
lista_elementos = []

# Função para criar um novo conjunto
def criar_conjunto(lista_nomes, lista_elementos):
    nome = input("Digite o nome do conjunto: ")

    # Verifica se o conjunto já existe
    if nome in lista_nomes:
        print("⚠️ Conjunto já existe")
        return

    elementos = []

    print("Digite os elementos inteiros (ou 'sair' para terminar):")

    elem = input("Elemento: ")

    # Loop para adicionar elementos até o usuário digitar 'sair'
    while elem != "sair":
        if int(elem) not in elementos:  # Evita elementos repetidos
            elementos.append(int(elem)) # Converte elem para int
        else:
            print("⚠️ Esse elemento já foi adicionado!")
        
        elem = input("Elemento: ")

    # Armazenar o nome e os elementos do conjunto criado nas listas.
    lista_nomes.append(nome)
    lista_elementos.append(elementos)
    print("✅ Conjunto criado com sucesso!")

# Função para adicionar um elemento a um conjunto existente
def adicionar_elemento(lista_nomes, lista_elementos):
    print("\n*~~*~~*~~* ➕ ADICIONAR ELEMENTO ➕ *~~*~~*~~*")
    
    nome = input("Digite o nome do conjunto: ")

    # Verifica se o conjunto existe
    if nome in lista_nomes:
        indice = lista_nomes.index(nome)
        elemento = int(input("Digite o elemento: "))

        if elemento not in lista_elementos[indice]:
            lista_elementos[indice].append(elemento)
            print("✅ Elemento adicionado com sucesso!")
        else:
            print("⚠️ Esse elemento já está no conjunto.")
    else:
        print("❌ Conjunto não encontrado.")
    
    print("*~~*~~*~~* ∎ FIM DA OPERAÇÃO ∎ *~~*~~*~~*\n")

# Função para remover um elemento de um conjunto
def remover_elemento(lista_nomes, lista_elementos):
    print("\n*~~*~~*~~* ➖ REMOVER ELEMENTO ➖ *~~*~~*~~*")
    
    nome = input("Digite o nome do conjunto: ")

    # Verifica se o conjunto existe
    if nome in lista_nomes:
        indice = lista_nomes.index(nome)
        elemento = int(input("Digite o elemento: "))

        if elemento in lista_elementos[indice]:
            lista_elementos[indice].remove(elemento)
            print("✅ Elemento removido com sucesso!")
        else:
            print("⚠️ Elemento não encontrado no conjunto.")
    else:
        print("❌ Conjunto não encontrado.")

    print("*~~*~~*~~* ∎ FIM DA OPERAÇÃO ∎ *~~*~~*~~*\n")

# Função para mostrar todos os conjuntos criados
def mostrar_conjuntos(lista_nomes, lista_elementos):
    if len(lista_nomes) == 0:
        print("========== ∅ Nenhum conjunto encontrado. ∅ ==========")
    else:
        print("\n========== ℂ CONJUNTOS CRIADOS ℂ ==========")
        # Percorre todos os conjuntos e exibe nome e elementos
        for i in range(len(lista_nomes)):
            print(f"➤ Conjunto '{lista_nomes[i]}': {lista_elementos[i]}")
        print("========== ∎ FIM ∎ =========°\n")

# Função para apagar um conjunto
def apagar_conjunto(lista_nomes, lista_elementos):    
    print("\n*~~*~~*~~* 🗑️ REMOVER CONJUNTO 🗑️ *~~*~~*~~*")
    
    nome = input("Digite o nome do conjunto: ")

    # Verifica se o conjunto existe
    if nome in lista_nomes:
        indice = lista_nomes.index(nome)
        lista_nomes.pop(indice)  # Remove o nome
        lista_elementos.pop(indice)  # Remove os elementos
        print(f"➤  ✅ Conjunto '{nome}' removido com sucesso!")
    else:
        print("❌ Conjunto não encontrado.")

    print("*~~*~~*~~* ∎ FIM DA OPERAÇÃO ∎ *~~*~~*~~*\n")

# Função para realizar a união de dois conjuntos
def unir_conjuntos(lista_nomes, lista_elementos):
    print("\n*~~*~~*~~* ∪ UNIÃO DE CONJUNTOS ∪ *~~*~~*~~*")

    nome1 = input("Digite o nome do primeiro conjunto: ")
    nome2 = input("Digite o nome do segundo conjunto: ")

    # Verifica se ambos os conjuntos existem
    if nome1 in lista_nomes and nome2 in lista_nomes:
        indice1 = lista_nomes.index(nome1)
        indice2 = lista_nomes.index(nome2)

        conjunto1 = lista_elementos[indice1]
        conjunto2 = lista_elementos[indice2]

        # Cria uma cópia do primeiro conjunto
        uniao = conjunto1.copy()
        
        # Adiciona elementos do segundo conjunto que não estão na união
        for elemento in conjunto2:
            if elemento not in uniao:
                uniao.append(elemento)

        print(f"✅ União de '{nome1}' ∪ '{nome2}': {uniao}")
    else:
        print("❌ Erro: um ou ambos os conjuntos não existem.")

    print("*~~*~~*~~* ∎ FIM DA OPERAÇÃO ∎ *~~*~~*~~*\n")

# Função para realizar a interseção de dois conjuntos
def interseccao_conjuntos(lista_nomes, lista_elementos):
    print("\n*~~*~~*~~* ∩ INTERSEÇÃO DE CONJUNTOS ∩ *~~*~~*~~*")

    nome1 = input("Digite o nome do primeiro conjunto: ")
    nome2 = input("Digite o nome do segundo conjunto: ")

    # Verifica se ambos os conjuntos existem
    if nome1 in lista_nomes and nome2 in lista_nomes:
        indice1 = lista_nomes.index(nome1)
        indice2 = lista_nomes.index(nome2)

        conjunto1 = lista_elementos[indice1]
        conjunto2 = lista_elementos[indice2]

        intersecao = []

        # Adiciona elementos que estão em ambos os conjuntos
        for elemento in conjunto1:
            if elemento in conjunto2:
                intersecao.append(elemento)

        print(f"✅ Interseção de '{nome1}' ∩ '{nome2}': {intersecao}")
    else:
        print("❌ Inválido, não foi encontrado um ou ambos os conjuntos.")

    print("*~~*~~*~~* ∎ FIM DA OPERAÇÃO ∎ *~~*~~*~~*\n")

# Loop principal para o funcionamento do menu
while True:
    menu()  # Mostra o menu
    opcao = input(">> Escolha uma opção: ")

    # Encaminha para a função escolhida
    if opcao == '1':
        criar_conjunto(lista_nomes, lista_elementos)
    elif opcao == '2':
        adicionar_elemento(lista_nomes, lista_elementos)
    elif opcao == '3':
        remover_elemento(lista_nomes, lista_elementos)
    elif opcao == '4':
        mostrar_conjuntos(lista_nomes, lista_elementos)
    elif opcao == '5':
        apagar_conjunto(lista_nomes, lista_elementos)
    elif opcao == '6':
        unir_conjuntos(lista_nomes, lista_elementos)
    elif opcao == '7':
        interseccao_conjuntos(lista_nomes, lista_elementos)
    elif opcao == '0':
        print(">> Você saiu do menu.")
        break  # Sai do loop e encerra o programa
    else:
        print(">> Opção inválida.")  # Tratamento de erro para opções inexistentes