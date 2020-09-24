class Funcionario():
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def aumenta_salario(self, salario=0, valor=0):
        print(salario + valor)


class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

    def aumenta_salario(self, salario, valor=20):
        print(salario + valor)


class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

    def aumenta_salario(self, salario, valor=20):
        print(salario + valor)


class test():
    programador = Programador("vinicius", 18, 1000)
    programador.aumenta_salario(1000, 20)
    analista = Analista("nicholai", 18, 2000)
    analista.aumenta_salario(2000)


test()
