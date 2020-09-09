def menu():
    print("1. listar alunos e suas notas finais;\n"
          "2. adicionar a nota final ao aluno;\n"
          "3. delete a nota final do aluno.")

dict = {
    "vinicius" : "",
    "maria" : "",
    "joao" : ""
}
while True:
    menu()
    opcao = int(input(":: "))

    if opcao == 1:
        print(dict)

    elif opcao == 2:
        aluno = int(input("qual aluno voce deseja escolher:\n"
                          "1. vinicius;\n"
                          "2. maria; \n"
                          "3. joao.\n"
                          ":: "))
        if aluno == 1:
            nota = float(input("digite a nova nota: "))
            dict["vinicius"] = nota

        elif aluno == 2:
            nota = float(input("digite a nova nota: "))
            dict["maria"] = nota

        elif aluno == 3:
            nota = float(input("digite a nova nota: "))
            dict["joao"] = nota

    elif opcao == 3:
        aluno = aluno = int(input("qual aluno voce deseja escolher:\n"
                          "1. vinicius;\n"
                          "2. maria; \n"
                          "3. joao.\n"
                          ":: "))
        if aluno == 1:
            dict["vinicius"] = ""

        elif aluno == 2:
            dict["maria"] = ""

        elif aluno == 3:
            dict["joao"] = ""




