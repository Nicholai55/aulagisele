from N2.classe_musica import Musica
from N2.conexao_mongo_musica import *
import pymongo

def menu():
    chave = 0

    while True:
        print("MENU \n"
              " 0. finalizar programa \n 1. cadastrar musica \n 2. consultar dados")
        opcao = int(input("Digite qual a opcao desejada: "))
        if opcao == 0:
            break
        elif opcao == 1:
            chave = 0
            while chave == 0:
                pergunta = input("Digite o nome da musica: ")
                if len(pergunta) < 150:
                    nome_musica = pergunta
                    chave = 1
                else:
                    print("Digite um valor valido")
            chave = 0
            while chave == 0:
                pergunta = input("Digite o autor da musica: ")
                if len(pergunta) < 150:
                    autor_musica = pergunta
                    chave = 1
                else:
                    print("Digite um valor valido")
            chave = 0
            while chave == 0:
                pergunta = input("Digite o genero da musica: ")
                if len(pergunta) < 150:
                    genero_musica = pergunta
                    chave = 1
                else:
                    print("Digite um valor valido")
            chave = 0
            musica = Musica(nome_musica, autor_musica, genero_musica)
            musica.mostrar()
            ConexaoMongo.salvar(nome_musica,autor_musica,genero_musica)
        elif opcao == 2:
            mongo = ConexaoMongo()
            mongo.listar()

menu()
