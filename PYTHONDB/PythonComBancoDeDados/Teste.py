import sqlite3

#1. Conectar com banco de dados
conexao = sqlite3.connect('Abobrinha.sqlite')
cursor = conexao.cursor()

#2. Inserir uma tabela com colunas
comando_DDL = '''CREATE TABLE IF NOT EXISTS produtos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
preco REAL
)'''

cursor.execute(comando_DDL)

#3. Inserir varias linhas em um insert
comando_DML_Insert = """
INSERT INTO produtos(nome, preco) VALUES
    ('camiseta', 49.90),
    ('calça', 120.00)
"""
cursor.execute(comando_DML_Insert)

comando_DML_Delete = """
DELETE FROM produtos
WHERE preco = 49.90
"""
cursor.execute(comando_DML_Delete)

conexao.commit()
conexao.close()