class Funcionario():
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def aumenta_salario(self, valor = 0):
        print(self.salario + valor)


class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

    def aumenta_salario(self, valor = 20):
        print("O salario de programador eh ", self.salario + valor)


class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

    def aumenta_salario(self, valor = 30):
        print("O salario de analista eh ", self.salario + valor)

class Teste():
    programador = Programador("vinicius", 18, 700)
    programador.aumenta_salario()
    analista = Analista("Nicholai", 18, 2000)
    analista.aumenta_salario()

class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print("O valor do ingresso eh: ", self.valor)

class IngressoVIP(Ingresso):
    def imprimeValor(self, adicional = 0.5):
        print("O valor do ingresso VIP eh: ", self.valor + (self.valor * adicional))

class Normal(Ingresso):
    def imprimeValor(self):
        print("O valor do ingresso eh: ", self.valor)

class CamaroteInferior(Ingresso, Funcionario):
    def imprimeValor(self):
        print("O valor do ingresso eh: ", self.valor)

    def localIngresso(self, local):
        print("A localizacao do ingresso eh: ", local)

    def aumenta_salario(self, valor = 0):
        print(self.salario + valor)

class CamaroteSuperior(IngressoVIP, Funcionario):
    def imprimeValor(self, adicional = 0.5):
        print("O valor do ingresso VIP eh: ", self.valor + (self.valor * adicional))

    def localIngresso(self, local):
        print("A localizacao do ingresso VIP eh: ", local)

    def aumenta_salario(self, valor = 0):
        print(self.salario + valor)

print("_________________________________________________\n")
camarote_sup = CamaroteSuperior(300)
camarote_sup.imprimeValor()
camarote_sup.localIngresso("Teatro")

camarote_inf = CamaroteInferior(300)
camarote_inf.imprimeValor()
camarote_inf.localIngresso("Teatro")

ingresso = Ingresso(300)
ingresso.imprimeValor()

ingresso2 = IngressoVIP(300)
ingresso2.imprimeValor()

ingresso3 = Normal(300)
ingresso3.imprimeValor()


