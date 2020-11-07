class Musica():
    def __init__(self, nome, autor, genero):
        self.nome = nome
        self.autor = autor
        self.genero = genero

    def mostrar(self):
        print("nome: {}, autor: {}, genero : {} ".format(self.nome,self.autor,self.genero))
