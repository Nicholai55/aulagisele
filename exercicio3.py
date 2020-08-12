class Calculadora():

    def inicio(self):
        print("INICIANDO")

    def calculo(self, numero1, numero2):
        calculo1 = numero1 + numero2
        calculo2 = numero1 - numero2
        calculo3 = numero1 / numero2
        calculo4 = numero1 * numero2
        print("soma:", calculo1, "\n""subtração:", calculo2, "\n"
              "divisão:", calculo3, "\n""multiplicação:", calculo4)


calculando = Calculadora()
calculando.inicio()
calculando.calculo(int(input("digite um numero: ")),
                   int(input("digite outro numero: ")))
