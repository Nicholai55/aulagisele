class Bicicleta():
    def __init__(self):
        print("---------------")

    def quantidadeMarchas(self, quantidade):
        self.quantidade = quantidade
        print("essa bicicleta tem {} marchas".format(quantidade))

    def tipoFreio(self, tipo):
        self.tipo = tipo
        print("o tipo de freio é:", tipo)

    def marca(self, qualmarca):
        self.qualmarca = qualmarca
        print("a marca dessa bicicleta é:", qualmarca)


class BicicletaPasseio(Bicicleta):
    def __init__(self):
        super().__init__()


class BicicletaProfissional(Bicicleta):
    def __init__(self):
        super().__init__()


bicicleta = BicicletaPasseio()
bicicleta.quantidadeMarchas(6)
bicicleta.tipoFreio("a disco")
bicicleta.marca("caloi")

goodbike = BicicletaProfissional()
goodbike.quantidadeMarchas(11)
goodbike.tipoFreio("a disco")
goodbike.marca("Specialized")
