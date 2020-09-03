def conta(notaUM, notaDOIS, notaTRES):
    print("A media do aluno foi: ")
    calculo = (notaUM + notaDOIS + notaTRES) / 3
    print(calculo)
    if calculo >= 6:
        print("APROVADO!")
    else:
        print("REPROVADO!")


while True:
    aluno = input("digite o nome do aluno: ")
    nota1 = int(input("digite a primeira nota: "))
    nota2 = int(input("digite a segunda nota: "))
    nota3 = int(input("digite a terceira nota: "))
    print(aluno, ":")
    conta(nota1, nota2, nota3)
