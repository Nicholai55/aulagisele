lista = [8, 3, 10, 15, 1]
print(lista)

soma = 0
for a in lista:
    soma = soma + a

print(soma)
media = soma / len(lista)
print(media)

def comparacao(list):

    avg = sum(list) / len(list)
    diffs = {value: abs(value - avg) for value in list}

    return min(diffs, key=diffs.get)

print(comparacao(lista))

