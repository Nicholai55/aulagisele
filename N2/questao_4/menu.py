from email_validator import validate_email, EmailNotValidError
from mongo.pessoa import Pessoa
from mongo.conexao import *

def menu():
    chave = 0

    while True:
        print("MENU \n"
              " 0. finalizar programa \n 1. cadastrar pessoa\n 2. editar dados pessoais\n 3. excluir dados pessoais\n 4. consultar dados")
        opcao = int(input("Digite qual a opcao desejada: "))
        if opcao == 0:
            break
        elif opcao == 1:
            chave = 0
            while chave == 0:
                pergunta = input("Digite o nome: ")
                if len(pergunta) < 150:
                    nome = pergunta
                    chave = 1
                else:
                    print("Digite um valor valido")
            chave = 0
            while chave == 0:
                pergunta = input("Digite o CPF(apenas os numeros): ")
                if len(pergunta) == 11:
                    if pergunta.isdigit() == True:
                        mongo = ConexaoMongo.connection()
                        print(mongo.find_one({"cpf" : pergunta}))
                        if mongo.find_one({"cpf" : pergunta}) == None:
                            cpf = pergunta
                            chave = 1
                        else:
                            print("Digite um valor valido")
                    else:
                        print("Digite um valor valido")
                else:
                    print("Digite um valor valido")
            chave = 0
            while chave == 0:
                pergunta = input("Digite o E-mail: ")
                if len(pergunta) < 400:
                    try:
                        valid = validate_email(pergunta)
                        mail = valid.email
                        if mail == pergunta:
                            email = pergunta
                            chave = 1
                        else:
                            print("Digite um e-mail valido")

                    except EmailNotValidError as error:
                        print(str(error))

                else:
                    print("Digite um email valido")
            chave = 0
            pessoa = Pessoa(nome, cpf, email)
            print("Nome: {}, CPF: {}, E-mail: {}".format(pessoa.nome, pessoa.cpf, pessoa.email))
            print("Deseja modificar algum dado?")
            pergunta = input('Digite "s" ou "n": ')
            if pergunta.lower() == "n":
                ConexaoMongo.salvar(nome, cpf, email)
            elif pergunta.lower() == "s":
                chave = 0
                while chave == 0:
                    pergunta = input("Digite o nome: ")
                    if len(pergunta) < 150:
                        nome = pergunta
                        chave = 1
                    else:
                        print("Digite um valor valido")
                chave = 0
                while chave == 0:
                    pergunta = input("Digite o CPF: ")
                    if len(pergunta) == 11:
                        if pergunta.isdigit() == True:
                            mongo = ConexaoMongo.connection()
                            if mongo.find_one({"cpf" : pergunta}) == None:
                                cpf = pergunta
                                chave = 1
                            else:
                                print("Digite um valor valido")
                        else:
                            print("Digite um valor valido")
                    else:
                        print("Digite um valor valido")
                chave = 0
                while chave == 0:
                    pergunta = input("Digite o E-mail: ")
                    if len(pergunta) < 400:
                        try:
                            valid = validate_email(pergunta)
                            mail = valid.email
                            if mail == pergunta:
                                email = pergunta
                                chave = 1
                            else:
                                print("Digite um valor valido")
                        except EmailNotValidError as error:
                            print(str(error))
                    else:
                        print("Digite um email valido")
                chave = 0
                pessoa = Pessoa(nome, cpf, email)
                ConexaoMongo.salvar(pessoa.nome, pessoa.cpf, pessoa.email)
        elif opcao == 2:
            print(" 1. Nome; \n 2. CPF; \n 3. E-mail;")
            tipo = int(input("Digite qual coluna de informacoes devera ser feita a troca"))
            valor_velho = input("Digite o valor que deve ser trocado: ")
            valor_novo = input("Digite o valor novo que sera adicionado: ")
            if tipo == 1:
                if len(valor_novo) < 150:
                    mongo = ConexaoMongo()
                    mongo.update(valor_velho, valor_novo, "nome")
                else:
                    print("Digite um valor valido")
            elif tipo == 2:
                if len(valor_novo) == 11:
                    if valor_novo.isdigit():
                        mongo = ConexaoMongo()
                        mongo.update(valor_velho, valor_novo, "cpf")
                        # if mongo.pesquisar("cpf", valor_novo) == "None":
                        #
                        # else: print("Digite um valor valido")
                    else:
                        print("Digite um valor valido")
                else:
                    print("Digite um valor valido")
            elif tipo == 3:
                if len(valor_novo) < 400:
                    try:
                        valid = validate_email(valor_novo)
                        mail = valid.email

                    except EmailNotValidError as error:
                        print(str(error))
                    mongo = ConexaoMongo()
                    mongo.update(valor_velho, valor_novo, "email")
        elif opcao == 3:
            print(" 1. Nome; \n 2. CPF; \n 3. E-mail;")
            tipo = int(input("Digite qual coluna sera o filtro: "))
            valor = input("Digite o valor que devera ser deletado: ")
            if tipo == 1:
                mongo = ConexaoMongo()
                try:
                    mongo = ConexaoMongo()
                    dado_deletado = mongo.pesquisar("nome", valor)
                    file = open("Dados_Deletados.txt", "a")
                    file.write(str(dado_deletado))
                    file.write("\n")
                    file.close()
                except Exception as error:
                    print("Erro ao salvar dado deletado", error)
                mongo.delete("nome", valor)
            elif tipo == 2:
                mongo = ConexaoMongo()
                try:
                    mongo = ConexaoMongo()
                    dado_deletado = mongo.pesquisar("cpf", valor)
                    file = open("Dados_Deletados.txt", "a")
                    file.write(str(dado_deletado))
                    file.write("\n")
                    file.close()
                except Exception as error:
                    print("Erro ao salvar dado deletado", error)
                mongo.delete("cpf", valor)
            elif tipo == 3:
                mongo = ConexaoMongo()
                try:
                    mongo = ConexaoMongo()
                    dado_deletado = mongo.pesquisar("email", valor)
                    file = open("Dados_Deletados.txt", "a")
                    file.write(str(dado_deletado))
                    file.write("\n")
                    file.close()
                except Exception as error:
                    print("Erro ao salvar dado deletado", error)
                mongo.delete("email", valor)
        elif opcao == 4:
            print(" 1. Nome; \n 2. CPF; \n 3. E-mail;")
            tipo = int(input("Digite qual coluna sera o filtro: "))
            pesquisa = input("Digite uma informacao da pessoa a ser pesquisada: ")
            if tipo == 1:
                mongo = ConexaoMongo()
                print(mongo.pesquisar("nome", pesquisa))
            elif tipo == 2:
                mongo = ConexaoMongo()
                print(mongo.pesquisar("cpf", pesquisa))
            elif tipo == 3:
                mongo = ConexaoMongo()
                print(mongo.pesquisar("email", pesquisa))
        elif opcao == 5:
            mongo = ConexaoMongo()
            mongo.listar()
menu()
