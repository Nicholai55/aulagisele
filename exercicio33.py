def menu():
    print("1. listar alunos e suas notas;\n"
          "2. adicionar ou modificar uma nota do aluno;\n"
          "3. delete uma nota do aluno;\n"
          "4. mostrar as medias dos alunos.")


class Aluno:
    def __init__(self, nome, n1, n2, n3, media):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.media = (n1 + n2 + n3) / 3

aluno1 = Aluno("vinicius", 10, 10, 10, 0)
aluno2 = Aluno("maria", 10, 9, 9, 0)
aluno3 = Aluno("joao", 5, 3, 6, 0)

while True:
    menu()
    opcao = int(input(":: "))

    if opcao == 1:
        print("alunos: \n"
              "nome: {} - {} / {} / {} \n"
              "nome: {} - {} / {} / {} \n"
              "nome: {} - {} / {} / {} \n".format(aluno1.nome, aluno1.n1, aluno1.n2, aluno1.n3, aluno2.nome, aluno2.n1, aluno2.n2, aluno2.n3, aluno3.nome, aluno3.n1, aluno3.n2, aluno3.n3))

    elif opcao == 2:

        print("1. vinicius; \n"
              "2. maria; \n"
              "3. joao. ")
        aluno = int(input("digite qual o aluno que voce deseja adicionar a nota:"))

        if aluno == 1:
            nota = float(input("digite a nota "))
            qual_nota = int(input("digite qual nota eh (1 = n1): "))
            if qual_nota == 1:
                aluno1.n1 = nota

            elif qual_nota == 2:
                aluno1.n2 = nota

            elif qual_nota == 3:
                aluno1.n3 = nota

        elif aluno == 2:
            nota = float(input("digite a nota "))
            qual_nota = int(input("digite qual nota eh (1 = n1): "))
            if qual_nota == 1:
                aluno2.n1 = nota

            elif qual_nota == 2:
                aluno2.n2 = nota

            elif qual_nota == 3:
                aluno2.n3 = nota

        elif aluno == 3:
            nota = float(input("digite a nota "))
            qual_nota = int(input("digite qual nota eh (1 = n1): "))
            if qual_nota == 1:
                aluno3.n1 = nota

            elif qual_nota == 2:
                aluno3.n2 = nota

            elif qual_nota == 3:
                aluno3.n3 = nota

    elif opcao == 3:
        print("1. vinicius; \n"
              "2. maria; \n"
              "3. joao. ")
        aluno = int(input("digite qual o aluno que voce deseja remover a nota:"))

        if aluno == 1:
            print(aluno1.nome)
            nota = int(input("qual nota sera excluida: "))
            if nota == 1:
                aluno1.n1 = 0

            elif nota == 2:
                aluno1.n2 = 0

            elif nota == 3:
                aluno1.n3 = 0

        elif aluno == 2:
            print(aluno2.nome)
            nota = int(input("qual nota sera excluida: "))
            if nota == 1:
                aluno2.n1 = 0

            elif nota == 2:
                aluno2.n2 = 0

            elif nota == 3:
                aluno2.n3 = 0

        elif aluno == 3:
            print(aluno3.nome)
            nota = int(input("qual nota sera excluida: "))
            if nota == 1:
                aluno3.n1 = 0

            elif nota == 2:
                aluno3.n2 = 0

            elif nota == 3:
                aluno3.n3 = 0

    elif opcao == 4:
        print("{} - {} \n"
              "{} - {} \n"
              "{} - {} \n".format(aluno1.nome, aluno1.media, aluno2.nome, aluno2.media, aluno3.nome, aluno3.media))
