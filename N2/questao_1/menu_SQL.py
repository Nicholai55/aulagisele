from N2.classe_musica import Musica
import psycopg2

def menu():
    chave = 0

    while True:
        print("MENU \n"
              " 0. finalizar programa \n 1. cadastrar musica\n 2. consultar dados")
        opcao = int(input("Digite qual a opcao desejada: "))
        if opcao == 0:
            break
        elif opcao == 1:
            chave = 0
            while chave == 0:
                pergunta = input("Digite o nomee da muscia: ")
                if len(pergunta) < 255:
                    nome_musica = pergunta
                    chave = 1
                else:
                    print("utilize um nome valido")
            chave = 0
            while chave == 0:
                pergunta = input("Digite o autor da musica: ")
                if len(pergunta) < 255:
                    autor_musica = pergunta
                    chave = 1
                else:
                    print("utilize um nome valido")
            chave = 0
            while chave == 0:
                pergunta = input("Digite o genero da musica: ")
                if len(pergunta) < 255:
                    genero_musica = pergunta
                    chave = 1
                else:
                    print("utilize um nome valido")

                musica = Musica(nome_musica,autor_musica,genero_musica)
                musica.mostrar()
                try:
                    connection = psycopg2.connect(user = "postgres",
                                                  password = "0410",
                                                  host = "localhost",
                                                  port = "5432",
                                                  database = "prova")
                    cursor = connection.cursor()
                    postgres_inser_query = '''INSERT INTO musica
                    (nome,autor,genero)
                    VALUES (%s, %s, %s)'''
                    record_to_insert = (nome_musica, autor_musica, genero_musica)
                    cursor.execute(postgres_inser_query, record_to_insert)
                    connection.commit()
                    print("Dados inseridos com sucesso")
                except (Exception, psycopg2.Error) as error:
                    if(connection):
                        print("Falha ao inserir dados na tabela", error)
                finally:
                    if(connection):
                        cursor.close()
                        connection.close()
                        print("conexao encerrada")
        elif opcao == 2:
            try:
                connection = psycopg2.connect(user = "postgres",
                                              password = "0410",
                                              host = "localhost",
                                              port = "5432",
                                              database = "prova")
                cursor = connection.cursor()
                select_query = "SELECT * FROM musica"
                cursor.execute(select_query)
                print("buscando dados")
                tabela_salva = cursor.fetchall()

                for row in tabela_salva:
                    print("id: ", row[0], "/ nome: ", row[1], "/ autor: ", row[2], "/ genero: ", row[3], "\n")
            except (Exception, psycopg2.Error) as error:
                print("Erro ao mostrar dados", error)
            finally:
                if(connection):
                    cursor.close()
                    connection.close()
                    print("Conexao encerrada")

menu()
