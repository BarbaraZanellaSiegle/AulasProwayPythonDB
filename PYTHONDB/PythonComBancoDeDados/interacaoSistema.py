from crud import animacao, interacaoBanco, listarTabela
import sqlite3

def menu():
    #bloco 01
    igual = "*"*20
    sistema = True

    #Bloco 02
    while sistema != False:

        #Bloco 03
        animacao()

        #Bloco 04
        print("Seja Bem Vindo a aula de Python com Banco de Dados!")

        nome = input("Informe seu nome: ")
        sobrenome = input("Informe seu sobrenome: ")
        idade = int(input("Informe sua idade: "))

        #Bloco 05
        conexao = sqlite3.connect("Abobrinha.sqlite")
        cursor = conexao.cursor()

        listarTabela(nome, sobrenome, cursor, conexao)

        interacaoBanco(nome, sobrenome, cursor, conexao)

        #Bloco 06
        continuaSistema = int(input(f"{nome}{sobrenome}, deseja continuar ou sair do sistema?\n(Digite 1 para Sim e 2 para Não)"))

        if continuaSistema == 2:     
            sistema = False

        elif continuaSistema == 1:     
            sistema = True

        else:
            print(f"O numero {continuaSistema} que você digitou não faz parte das opções fornecidas")
            sistema = False

    #Bloco 07
    animacao()
    print("Você saiu do sistema")       
    conexao.close()