from time import sleep
import _sqlite3


sistema = True
while sistema != False:

    for animacao in range(20):
        sleep(0.1)
        print("*")

    print("Seja Bem Vindo a aula de Python com Banco de Dados!")

    nome = input("Informe seu nome: ")
    sobrenome = input("Informe seu sobrenome: ")
    idade = int(input("Informe sua idade: "))

    conexao = _sqlite3.connect("Abobrinha.sqlite")

    cursor = conexao.cursor()

    repeticao = True



    while repeticao != False:

        novaTabela = int(input(f"{nome}{sobrenome}, deseja criar uma nova tabela?\n(Digite 1 para Sim e 2 para Não)"))

        if novaTabela == 2:     
            repeticao = False

        elif novaTabela == 1:
            repeticao = True

            nomeTabela = input(f"{nome}{sobrenome}, informe o nome da tabela que desejas criar:> ")

            comandoCriaTabela = f'''
            CREATE TABLE IF NOT EXISTS {nomeTabela} (
                id INTEGER,
                nome TEXT NOT NULL
            )
            '''

            cursor.execute(comandoCriaTabela)

            conexao.commit()

            desejaDeletar = True

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



    continuaSistema = int(input(f"{nome}{sobrenome}, deseja continuar ou sair do sistema?\n(Digite 1 para Sim e 2 para Não)"))

    if continuaSistema == 2:     
        sistema = False

    elif continuaSistema == 1:     
        sistema = True

    else:
        print(f"O numero {continuaSistema} que você digitou não faz parte das opções fornecidas")
        sistema = False


print("Você saiu do sistema")
        
conexao.close()


