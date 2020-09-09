mulher1 = int(input("Digite a idade da primeira mulher:"))
mulher2 = int(input("Digite a idade da segunda mulher:"))
homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input("Digite a idade do segundo homem: "))

lista_mulheres = [mulher1, mulher2]
lista_homens = [homem1, homem2]

lista_mulheres.sort()
lista_homens.sort()

print(lista_homens[1] + lista_mulheres[0])
print(lista_homens[0] * lista_mulheres[1])
