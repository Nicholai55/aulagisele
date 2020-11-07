import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "0410",
                                  host = "localhost",
                                  port = "5432",
                                  database = "prova")
    cursor = connection.cursor()

    create_tabble_query = '''CREATE TABLE musica(
    id SERIAL NOT NULL,
    nome VARCHAR(255),
    autor VARCHAR(255),
    genero VARCHAR(255)
    );'''

    cursor.execute(create_tabble_query)
    connection.commit()
    print("Tabela criada com sucesso no PostgreSQL")
except (Exception, psycopg2/DatabaseError) as error:
    print("erro ao criar tabela no PostgreSQL", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("conexao encerrada")
