from mongo.conexao import ConexaoMongo

class Pessoa():
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def save(self):
        conexao = ConexaoMongo()
        pessoa = {"nome" : self.nome, "cpf" : self.cpf, "email" : self.email}
        conexao.salvar(pessoa)
