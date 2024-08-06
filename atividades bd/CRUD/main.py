import sqlite3
from menu import menu
import conexao
import cadastrar_cliente
import select
import tabela
import update
import deletar

#Criação da tabela cliente
tabela.criar_tabela()

opcao = menu()
while (opcao != '6'):
    if(opcao == '1'):
        cadastrar_cliente.cadastro()
    elif(opcao == '2'):
        select.exibirCliente()
    elif(opcao == '3'):
        select.consultar_CPF()
    elif(opcao == '4'):
        update.alterarDados()
    elif(opcao == '5'):
        deletar.deletarDado()
    opcao = menu()
