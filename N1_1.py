lista = []
while True:
    recebe_lista = int(input(
        "digite os numeros de rebeldes ou digite 0 para sair: "))
    if recebe_lista > 0:
        lista.append(recebe_lista)
    else:
        print(lista)
        break


def maiornumero(l):
    meunumero_maior = l[0]
    for num in l:
        if meunumero_maior < num:
            meunumero_maior = num
    return meunumero_maior


def menornumero(l):
    meunumero_menor = l[0]
    for num in l:
        if meunumero_menor > num:
            meunumero_menor = num
    return meunumero_menor


def media(l):
    soma = 0
    for a in l:
        soma = soma + a

    media = soma / len(lista)
    return media

def comparacao(list):

    avg = sum(list) / len(list)
    diffs = {value: abs(value - avg) for value in list}

    return min(diffs, key=diffs.get)


print("esse é o menor numero", menornumero(lista))
print("esse é o maior numero", maiornumero(lista))
print("essa é a media", media(lista))
print("esse é o numero mais proximo da media", comparacao(lista))
