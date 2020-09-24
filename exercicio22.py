class Imovel():
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def imprimir_informacoes(self):
        print("endereco: {}, preco: {}".format(self.endereco, self.preco))

class NovoImovel(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco,preco)
        self.adicional = adicional

    def imprimir_informacoes(self):
        print("endereco: {}, preco: {}".format(self.endereco, self.preco + self.adicional))

class VelhoImovel(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def imprimir_informacoes(self):
        print("endereco: {}, preco: {}".format(self.endereco, self.preco - self.desconto))


imovel_novo = NovoImovel("Rua Teste de Teste, Nº 1880", 15000, 1000)
imovel_novo.imprimir_informacoes()

imovel = Imovel("Rua Teste de teste, Nº 1035", 10000)
imovel.imprimir_informacoes()

imovel_velho = VelhoImovel("Rua Teste de Teste, Nº 150", 9000, 500)
imovel_velho.imprimir_informacoes()
