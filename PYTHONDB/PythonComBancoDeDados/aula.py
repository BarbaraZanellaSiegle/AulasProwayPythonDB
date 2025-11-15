import _sqlite3

conexao = _sqlite3.connect("Abobrinha.sqlite")
cursor = conexao.cursor()

comando = "SELECT name FROM sqlite_master where type'table';"

cursor.execute(comando)

tabelas = cursor.fetchall()

if tabelas:
    for tabela in tabelas:
        print("Tabela", tabela[0])
    else:
        print("Nenhuma Tabela encontrada no banco atual")

conexao.close()