class Animal():

    def __init__(self):
        #print("INICIANDO O ATAQUE!!!")
        pass

    def comer(self):
        print("o animal esta comendo")


class Cachorro(Animal):
    def __init__(self):
        super().__init__()

    def comer(self):
        print("o animal esta comendo ração")


class Cavalo(Animal):
    def __init__(self):
        super().__init__()

    def comer(self):
        print("o animal esta comendo feno")


class Gato(Animal):
    def __init__(self):
        super().__init__()

    def comer(self):
        print("o animal esta comendo atum")


class AnimalTeste():
    def executando(self):
        cachorro = Cachorro()
        cavalo = Cavalo()
        gato = Gato()
        lista_animais = [cachorro, cavalo, gato]

        for i in lista_animais:
            i.comer()


teste_animal = AnimalTeste()
teste_animal.executando()
