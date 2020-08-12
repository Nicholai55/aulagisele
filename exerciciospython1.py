class Maiordeidade():
    def metodo1(self):
        print("iniciando")

    def testeidade(self, idade):
        if idade >= 18:
            print("essa pessoa é maior de idade!")
        else:
            print("essa pessoa é menor de idade!")
        return idade


pessoa = Maiordeidade()
pessoa.metodo1()
pessoa.testeidade(int(input("qual a sua idade: ")))
