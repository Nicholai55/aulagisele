from CRUD_local.classe_pessoa import*

lista_cadastro = []
lista_total = []
lista_excluidos = []
chave = 0

while True:
    print("MENU \n"
          "0. finalizar programa \n"
          "1. cadastrar pessoa\n"
          "2. editar dados pessoais\n"
          "3. excluir dados pessoais\n"
          "4. consultar dados")
    opcao = int(input("Digite qual a opcao desejada: "))

    if opcao == 1:
        chave = 0
        while chave == 0:
            pergunta = input("Digite seu nome: ")
            if len(pergunta) < 150:
                nome = pergunta
                chave = 1
            else:
                print('digite um valor valido')
        chave = 0
        while chave == 0:
            pergunta = input("Digite seu cpf: ")
            if pergunta in lista_total:
                print("Este cpf ja foi cadastrado, digite um cpf valido")
            else:
                if len(pergunta) == 11:
                    cpf = pergunta
                    chave = 1
                else:
                    print("Digite um cpf valido")
        chave = 0
        while chave == 0:
            pergunta = input("Digite seu e-mail: ")
            if len(pergunta) < 400:
                email = pergunta
                chave = 1
            else:
                print("Digite um e-mail valido")

        eu = Pessoa(nome, cpf, email)
        print(eu.nome, eu.cpf, eu.email)

        print("deseja modificar algum dado colocado:")
        pergunta = input("(Digite 's' ou 'n': ")
        if pergunta == "s":
            chave = 0
            while chave == 0:
                pergunta = input("Digite seu nome: ")
                if len(pergunta) < 150:
                    nome = pergunta
                    chave = 1
                else:
                    print("Digite um nome valido")
            chave = 0
            while chave == 0:
                pergunta = input("Digite seu cpf: ")
                if pergunta in lista_total:
                    print("Este cpf ja foi cadastrado, digite um cpf valido")
                else:
                    if len(pergunta) == 11:
                        cpf = pergunta
                        chave = 1
                    else:
                        print("Digite um cpf valido")
            chave = 0
            while chave == 0:
                pergunta = input("Digite seu e-mail: ")
                if len(pergunta) < 400:
                    email = pergunta
                    chave = 1
                else:
                    print("Digite um e-mail valido")
            chave = 0
            eu = Pessoa(nome, cpf, email)
            print(eu.nome, eu.cpf, eu.email)

            lista_total.append(eu.nome)
            lista_total.append(eu.cpf)
            lista_total.append(eu.email)

        elif pergunta == "n":
            lista_total.append(eu.nome)
            lista_total.append(eu.cpf)
            lista_total.append(eu.email)

    elif opcao == 2:
        cpf = input("Digite o cpf da pessoa a ser modificada: ")
        posicao_lista = lista_total.index(cpf)
        print(posicao_lista)

        pessoa = Pessoa(lista_total[posicao_lista - 1], lista_total[posicao_lista], lista_total[posicao_lista + 1])
        print(pessoa.nome, pessoa.cpf, pessoa.email)
        pergunta2 = int(input("qual informacao sera corrigida: \n"
                         "1. nome \n"
                         "2. cpf \n"
                         "3. e-mail \n"
                         "Digite: "))
        chave = 0
        if pergunta2 == 1:
            while chave == 0:
                novo_nome = input("Digite o nome correto: ")
                if len(novo_nome) < 150:
                    pessoa.nome = novo_nome
                    chave = 1
                    lista_total.pop(posicao_lista -1)
                    lista_total.insert(posicao_lista -1, novo_nome)
                else:
                    print("Digite um nome valido")
            chave = 0
        elif pergunta2 == 2:
            while chave == 0:
                pergunta = input("Digite seu cpf: ")
                if pergunta in lista_total:
                    print("Este cpf ja foi cadastrado, digite um cpf valido")
                else:
                    if len(pergunta) == 11:
                        cpf = pergunta
                        chave = 1
                    else:
                        print("Digite um cpf valido")
            chave = 0
        elif pergunta2 == 3:
            while chave == 0:
                novo_email = input("Digite o e-mail correto: ")
                if len(novo_nome) < 150:
                    pessoa.email = novo_email
                    chave = 1
                    lista_total.pop(posicao_lista + 1)
                    lista_total.insert(posicao_lista + 1, novo_email)
                else:
                    print("Digite um nome valido")
            chave = 0

    elif opcao == 3:
        cpf = input("Digite o cpf da pessoa a ser deletada: ")
        posicao_lista = lista_total.index(cpf)
        print(posicao_lista)

        lista_excluidos.append(lista_total[posicao_lista-1])
        lista_excluidos.append(lista_total[posicao_lista])
        lista_excluidos.append(lista_total[posicao_lista+1])
        lista_total.pop(posicao_lista - 1)
        lista_total.pop(posicao_lista - 1)
        lista_total.pop(posicao_lista - 1)

        print(lista_total)
        print(lista_excluidos)

    elif opcao == 4:
        pergunta = int(input("qual sera o filtro de pesquisa: \n"
                         "1. nome \n"
                         "2. cpf \n"
                         "3. e-mail \n"
                         "Digite: "))
        if pergunta == 1:
            nome = input("Digite o nome: ")
            posicao_lista = lista_total.index(nome)
            print(posicao_lista)
            print(lista_total[posicao_lista])
            print(lista_total[posicao_lista + 1])
            print(lista_total[posicao_lista + 2])

        elif pergunta == 2:
            cpf = input("Digite o cpf: ")
            posicao_lista = lista_total.index(cpf)
            print(posicao_lista)
            print(lista_total[posicao_lista - 1])
            print(lista_total[posicao_lista])
            print(lista_total[posicao_lista + 1])

        elif pergunta == 3:
            email = input("Digite o e-mail: ")
            posicao_lista = lista_total.index(email)
            print(posicao_lista)
            print(lista_total[posicao_lista - 2])
            print(lista_total[posicao_lista - 1])
            print(lista_total[posicao_lista])

    elif opcao == 5:
        print("lista total", lista_total)
        print("lista de excluidos", lista_excluidos)

    elif opcao == 0:
        break





