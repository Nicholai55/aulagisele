from random import *

lista1 = []
lista2 = []

while len(lista1) < 20:
    numero = randint(0,50)
    lista1.append(numero)
                # professora, deixei comentado um dos metodos comentado, da maneira qque esta agora,
                # o resultado sera True, porem, se comentar a linha 16 e descomentar as linhas 12 - 14, o resultado sera False

#while len(lista2) < 20:
#    numero = randint(0,50)
#    lista2.append(numero)

lista2 = lista1.copy()

if lista1 == lista2:
    validacao = True
    print(validacao)
elif lista1 != lista2:
    validacao = False
    print(validacao)

