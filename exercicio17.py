lista_nomes = []

while (len(lista_nomes) + 1) <= 5:
    pega_nomes = input("digite um nome: ")
    lista_nomes.append(pega_nomes)

tupla_nomes = (lista_nomes)

for j in tupla_nomes:
    print(j)
