import sqlite3

#1 passo Interacao com usuário
#nome = input("Digite o Nome que deseja dar para seu Banco :> ")
#conexao = sqlite3.connect(f"{nome}.sqlite")


# cria um novo banco ou conecta a um banco existente
conexao = sqlite3.connect("WilliamPB.sqlite")


#funcao Sqlite de manipulação de script SQL
cursor = conexao.cursor()

comandoSQL = '''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER,
    nome TEXT NOT NULL
)
'''

cursor.execute(comandoSQL)
conexao.commit()
conexao.close()


#Passo Algoritmo para criação do banco



