from time import sleep

def animacao():
    for animacao in range(20):
        sleep(0.1)
        print("*")


def listarTabela(nome, sobrenome, cursor, conexao):
    comando = "SELECT name FROM sqlite_master where type='table';"
    cursor.execute(comando)

    tabelas = cursor.fetchall()

    if tabelas:
        for tabela in tabelas:
            print("Tabela", tabela[0])
    else:
        print("Nenhuma Tabela encontrada no banco atual")


def interacaoBanco(nome, sobrenome, cursor, conexao):
    repeticao = True

    while repeticao != False:

        novaTabela = int(input(f"{nome}{sobrenome}, deseja criar uma nova tabela?\n(Digite 1 para Sim e 2 para Não)"))

        if novaTabela == 2:     
            repeticao = False

        elif novaTabela == 1:
            repeticao = True

            #INICIO
            nomeTabela = input(f"{nome}{sobrenome}, informe o nome da tabela que desejas criar:> ")
            #Lista onde as colunas serão guardadas
            colunas = []
            # Como seu exemplo tinha 2 colunas, vamos pedir exatamente2
            for i in range(1, 3):
                print(f"\n--- Coluna {i} ---")
                nomeColuna = input(f"{nome}, informe o nome da coluna {i}: ")

                print("\n INTEGER\n TEXT\n REAL\n NUMERIC\n")
                tipoColuna = input(f"{nome}, informe o tipo da coluna {i}: ")

                print("\n NOT NULL \nNULL")
                colunaVazio = input(f"{nome}, informe se a coluna pode ser nula ou não: ")

                # Monta a coluna
                colunas.append(f"{nomeColuna} {tipoColuna} {colunaVazio}")

            # Junta tudo no comando SQL
            comandoCriaTabela = f'''
            CREATE TABLE IF NOT EXISTS {nomeTabela} (
                {', '.join(colunas)}
            )
            '''

            cursor.execute(comandoCriaTabela)
            conexao.commit()
            desejaDeletar = True
            #FIM


            #ANTES
            # nomeTabela = input(f"{nome}{sobrenome}, informe o nome da tabela que desejas criar:> ")

            # comandoCriaTabela = f'''
            # CREATE TABLE IF NOT EXISTS {nomeTabela} (
            #     id INTEGER,
            #     nome TEXT NOT NULL
            # )
            # '''

            # cursor.execute(comandoCriaTabela)
            # conexao.commit()
            # desejaDeletar = True



            while desejaDeletar != False:

                deleta = int(input(f"{nome}{sobrenome}, deseja deletar a tabela?\n(Digite 1 para Sim e 2 para Não)"))
                
                if deleta == 1:
                    desejaDeletar = False
                    comandoDeletaTabela = f'''
                        DROP TABLE {nomeTabela}
                        '''  
                    print(F"Tabela {nomeTabela} EXCLUIDA!")

                    cursor.execute(comandoDeletaTabela)
                    conexao.commit()
            
            
                elif deleta == 2:
                    desejaDeletar = False
                    print(f"A tabela {nomeTabela} não será excluida")
                    
                
                else:
                    print(f"O numero {deleta} que você digitou não faz parte das opções fornecidas")
                    desejaDeletar = True


        else:
            repeticao = True
            print(f"O numero {novaTabela} que você digitou não faz parte das opções fornecidas")


