import sqlite3
from menu import menu
import conexao
import cadastrar_cliente
import select
import tabela
import update


def alterarDados():
    conexao.conectar_banco()
    global cpfPesquisar
    cpfPesquisar = select.consultar_CPF()
    verificaCPF = "SELECT * FROM cliente WHERE cpf = ?"
    conexao.cursor.execute(verificaCPF)
    resultado = conexao.cursor.fetchone()
def atualizar():
        try:
            consultaCPF = input("Qual o CPF do cliente que deseja alterar? ")
            verificaCPF = "SELECT * FROM cliente WHERE cpf = ?"
            conexao.cursor.execute(verificaCPF, (consultaCPF,))
            resultado = conexao.cursor.fetchone()

            if resultado:
                option = input("Qual dado você deseja alterar? (1 - para nome, 2 - para sobrenome, 3 - para idade, 4 - para CPF, 5 - para telefone, 6 - para endereço, 7 - para cidade e 8 - para estado): ")
            
                if option == '1':
                    novo_nome = input("Informe seu nome: ")
                    query = "UPDATE cliente SET nome = ? WHERE cpf = ?"
                    conexao.cursor.execute(query, (novo_nome, consultaCPF))
            
                elif option == '2':
                    novo_sobrenome = input("Informe seu sobrenome: ")
                    query = "UPDATE cliente SET sobrenome = ? WHERE cpf = ?"
                    conexao.cursor.execute(query, (novo_sobrenome, consultaCPF))
            
                elif option == '3':
                    nova_idade = int(input("Informe sua idade: "))
                    query = "UPDATE cliente SET idade = ? WHERE cpf = ?"
                    conexao.cursor.execute(query, (nova_idade, consultaCPF))
            
                elif option == '4':
                    novo_cpf = input("Informe seu novo CPF: ")
                    query = "UPDATE cliente SET cpf = ? WHERE cpf = ?"
                    conexao.cursor.execute(query, (novo_cpf, consultaCPF))
            
                elif option == '5':
                    novo_telefone = input("Informe seu telefone: ")
                    query = "UPDATE cliente SET telefone = ? WHERE cpf = ?"
                    conexao.cursor.execute(query, (novo_telefone, consultaCPF))
            
                elif option == '6':
                    novo_endereco = input("Informe seu endereço: ")
                    query = "UPDATE cliente SET endereco = ? WHERE cpf = ?"
                    conexao.cursor.execute(query, (novo_endereco, consultaCPF))
            
                elif option == '7':
                    nova_cidade = input("Informe sua cidade: ")
                    query = "UPDATE cliente SET cidade = ? WHERE cpf = ?"
                    conexao.cursor.execute(query, (nova_cidade, consultaCPF))
            
                elif option == '8':
                    novo_estado = input("Informe seu estado: ")
                    query = "UPDATE cliente SET estado = ? WHERE cpf = ?"
                    conexao.cursor.execute(query, (novo_estado, consultaCPF))
            
                conexao.conn.commit()  # Confirma as mudanças no banco de dados
                print("Dados atualizados com sucesso.")
            else:
                print("Cliente não encontrado.")
    
        except sqlite3.Error as e:
            print(f"Erro ao atualizar dados: {e}")
    

       """   
        if opcaoDeletar == 'nome':
            DelNome = input("Qual o nome a ser excluído? ")
            conexao.cursor.execute(f"DELETE FROM cliente WHERE cpf = 'valor_cpf';")
        elif opcaoDeletar == '2':
            DelIdade = int(input("Qual a idade a ser excluída? "))
            conexao.cursor.execute(f"DELETE FROM pessoas WHERE idade = {DelIdade}")
        elif opcaoDeletar == '3':
            DelEmail = input("Qual o email a ser excluído? ")
            conexao.cursor.execute(f"DELETE FROM pessoas WHERE email = '{DelEmail}'")
        else:
            print("Opção inválida")
         """