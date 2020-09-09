from random import *

lista_numeros = []
lista_principal = lista_numeros.copy()
lista_aux = []
contador = 0

while len(lista_numeros) < 20:
    numero = randint(0,50)
    lista_numeros.append(numero)
print(lista_numeros)

metade = float(len(lista_numeros) / 2)
print(metade)



while contador < metade:
    lista_aux.append(lista_numeros[contador])
    contador +=1

print(lista_aux)

for a in range(0,10):
    lista_numeros.pop(0)

for x in lista_aux:
    lista_numeros.append(x)

print(lista_principal)
print(lista_numeros)




