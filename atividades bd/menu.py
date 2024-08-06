import connect
import create_tabela
import selecionar
import insert
import delete


connect.conectar_banco()
create_tabela.criacao_tabela()
opcao = input("Bem-vindo à parte da manipulação do banco. Selecione 1 - para usar o select, 2 - para inserir os valores e 3 - para deletar os dados ")
while (opcao != 0):
    opcao = input("Bem-vindo à parte da manipulação do banco. Selecione 1 - para usar o select, 2 - para inserir os valores e 3 - para deletar os dados ")
    if opcao == '1':
            selecionar.select()
    elif opcao == '2':
            insert.inserir()
    elif opcao == '3':
            delete.deletar()


