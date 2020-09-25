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

# Decorator
# Decorator é um padrão de projeto de software que permite adicionar um comportamento a um objeto já existente em tempo de execução,
# ou seja, agrega dinamicamente responsabilidades adicionais a um objeto. Decorators oferecem uma alternativa flexível
# ao uso de herança para estender uma funcionalidade, com isso adiciona-se uma responsabilidade ao objeto e não à classe.
#
#Padrões de projeto
# Padrões de projeto podem ser vistos como uma solução que já foi testada para um problema, dessa forma reutilizamos a experiência
# de outros desenvolvedores que tiveram problemas semelhantes. Portanto, um padrão de projeto geralmente descreve uma solução ou
# uma instância da solução que foi utilizada para resolver um problema específico. Padrões de projetos são soluções para problemas
# que alguém um dia teve e resolveu aplicando um modelo que foi documentado e que você pode adaptar integralmente ou de acordo com
# a necessidade da sua solução, são melhores práticas formalizadas que o programador pode usar para resolver problemas comuns quando projetar uma aplicação ou sistema.
