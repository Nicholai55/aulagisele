from pymongo import MongoClient

class ConexaoMongo:
    def connection():
        try:
            client = MongoClient('localhost', 27017)
            banco = client.prova #nome do banco = prova
            colecao = banco.musica # nome da colecao = musica

            return colecao

        except Exception as error:
            print("erro ao conectar ao mongo")
            print(error)

    def salvar(nome, autor, genero): # json
        try:
            colecao = ConexaoMongo.connection()
            # id = colecao.insert_one(json).inserted_id

            query = {"nome" : nome, "autor" : autor, "genero" : genero}
            id = colecao.insert_one(query).inserted_id

        except Exception as error:
            print("problema ao salvar dados")
            #print(json)
            print(error)

    def update(self, informacao_antiga, informacao_noma, coluna):
        try:
            colecao = ConexaoMongo.connection()

            query = {coluna : informacao_antiga}
            novo_valor = {"$set" : {coluna : informacao_noma}}
            colecao.update_one(query, novo_valor)

        except Exception as error:
            print("problema ao modificar os dados")
            print(error)

    def delete(self, coluna, informacao):
        try:
            colecao = ConexaoMongo.connection()

            query = {coluna : informacao}
            colecao.delete_one(query)

        except Exception as error:
            print("problema ao deletar os registros")
            print(error)

    def pesquisar(self, coluna, informacao):
        try:
            colecao = ConexaoMongo.connection()

            print(colecao.find_one({coluna : informacao}))

        except Exception as error:
            print("Problema ao consultar os dados ")
            print(error)

    def listar(self):
        try:
            colecao = ConexaoMongo.connection()

            for a in colecao.find():
                print(a)

        except Exception as error:
            print("Problema ao consultar os dados ")
            print(error)

ConexaoMongo.connection()
