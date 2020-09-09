from random import *

lista_numeros1 = []
while len(lista_numeros1) < 20:
    numero = randint(0,50)
    lista_numeros1.append(numero)

lista_numeros2 = []
while len(lista_numeros2) < 20:
    numero = randint(0,50)
    lista_numeros2.append(numero)

print(lista_numeros1)
print(lista_numeros2)

lista3 = lista_numeros1 + lista_numeros2
print(lista3)
lista4 = []

contador = 0
while contador < 20:
    lista4.append(lista_numeros1[contador])
    lista4.append(lista_numeros2[contador])
    contador += 1



print(lista4)
