from random import *

lista_numeros = []
while len(lista_numeros) < 20:
    numero = randint(0,50)
    lista_numeros.append(numero)


numero1 = lista_numeros[0]
contador = 0
for b in lista_numeros:
    if b == numero1:
        contador +=1
    else:
        pass

print("total de numeros na lista ", len(lista_numeros))

soma = 0
for a in lista_numeros:
    soma += a





lista_numeros.sort()
lista_numeros.reverse()

print("A. maior numero = {}".format(lista_numeros[0]))
print("B. soma = {}".format(soma))
print("C. contador de repeticoes do primeiro numero = {}".format(contador))
print("D. media = {}".format(soma / 20))
