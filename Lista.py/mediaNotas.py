def calcMedia(Lnota : list):
    soma = 0
    for nota in Lnota:
        soma += nota

    media = soma / len(Lnota)
    return media

Lnota = [7, 7.5, 8, 10, 5.5]
media = calcMedia(Lnota)
print(f"Media: {media}")