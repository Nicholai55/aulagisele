import datetime
from random import randint

def calculo_tempo(function):
    def calculo():
        print(datetime.datetime.now())

        function()

        print(datetime.datetime.now())

    return calculo()

lista = []
while len(lista) < 4:
    numero = randint(1, 100)
    lista.append(numero)
print(lista)

@calculo_tempo
def funcao():
    soma = 0
    for a in lista:
        soma += a
    print(soma)

funcao


#
#
#
#
#
#
#
