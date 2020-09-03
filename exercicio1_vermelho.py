def conta(notaUM, notaDOIS, notaTRES):
    print("A media do aluno foi: ")
    calculo = (notaUM + notaDOIS + notaTRES) / 3
    print(calculo)
    if calculo >= 6:
        print("APROVADO!")
    else:
        print("REPROVADO!")


aluno1 = input("Digite o nome do aluno: ")
notaAluno1_1 = int(input("digite uma nota: "))
notaAluno1_2 = int(input("digite outra nota: "))
notaAluno1_3 = int(input("digite outra nota: "))

aluno2 = input("Digite o nome do aluno: ")
notaAluno2_1 = int(input("digite uma nota: "))
notaAluno2_2 = int(input("digite outra nota: "))
notaAluno2_3 = int(input("digite outra nota: "))

aluno3 = input("Digite o nome do aluno: ")
notaAluno3_1 = int(input("digite uma nota: "))
notaAluno3_2 = int(input("digite outra nota: "))
notaAluno3_3 = int(input("digite outra nota: "))

aluno4 = input("Digite o nome do aluno: ")
notaAluno4_1 = int(input("digite uma nota: "))
notaAluno4_2 = int(input("digite outra nota: "))
notaAluno4_3 = int(input("digite outra nota: "))

aluno5 = input("Digite o nome do aluno: ")
notaAluno5_1 = int(input("digite uma nota: "))
notaAluno5_2 = int(input("digite outra nota: "))
notaAluno5_3 = int(input("digite outra nota: "))

print(aluno1, ": ")
conta(notaAluno1_1, notaAluno1_2, notaAluno1_3)
print(aluno2, ": ")
conta(notaAluno2_1, notaAluno2_2, notaAluno2_3)
print(aluno3, ": ")
conta(notaAluno3_1, notaAluno3_2, notaAluno3_3)
print(aluno4, ": ")
conta(notaAluno4_1, notaAluno4_2, notaAluno4_3)
print(aluno5, ": ")
conta(notaAluno5_1, notaAluno5_2, notaAluno5_3)
