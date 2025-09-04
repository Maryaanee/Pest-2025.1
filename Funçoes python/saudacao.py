def saudacao(nome : str, idade : int = 0):
    print(f"Olá, {nome}! Você tem {idade} anos. Bem-vindo(a) a aula de funçôes!.")

saudacao("Lucas, 25")
saudacao("Ana", 30)
saudacao(idade=30, nome="João")
saudacao("Maria")