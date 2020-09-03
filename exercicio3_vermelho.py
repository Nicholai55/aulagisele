class Calculadora():

    def inicio(self):
        print("INICIANDO")

    def calculo(self, numero1, numero2):
        calculo1 = numero1 + numero2
        calculo2 = numero1 - numero2
        calculo3 = numero1 / numero2
        calculo4 = numero1 * numero2
        print("soma + 1:", calculo1 + 1, "\n""subtração + 1:", calculo2 + 1, "\n"
              "divisão + 1:", calculo3 + 1, "\n""multiplicação + 1:", calculo4 + 1)


calculando = Calculadora()
calculando.inicio()
calculando.calculo(int(input("digite um numero: ")),
                   int(input("digite outro numero: ")))
