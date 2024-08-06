import sqlite3
import tabela
import select
import conexao

def alterarDados():
    try:
        conexao.conectar_banco()
        print("######### Alteração de dados ########")
        global cpfPesquisar
        cpfPesquisar = select.consultar_CPF()

        if cpfPesquisar != []:
            dado_update = input("O que deseja alterar\nNome\nSobrenome\nIdade\nTelefone\nEndereco\nCidade\nEstado\n ").lower()
            atualizacao(dado_update)
        else:
            print("CPF não encontrado.")
    
    except sqlite3.Error as erro:
        print(f"Erro ao alterar dados: {erro}")

def atualizacao(dado_update):
    try:
        if dado_update == 'nome':
            novo_nome = input("Novo Nome: ")
            conexao.cursor.execute("UPDATE cliente SET nome = ? WHERE cpf = ?", (novo_nome, cpfPesquisar))
            print("Nome alterado com sucesso !!")
        
        elif dado_update == 'sobrenome':
            novo_sobrenome = input("Novo Sobrenome: ")
            conexao.cursor.execute("UPDATE cliente SET sobrenome = ? WHERE cpf = ?", (novo_sobrenome, cpfPesquisar))
            print("Sobrenome alterado com sucesso !!")
        
        elif dado_update == 'idade':
            nova_idade = int(input("Nova Idade: "))
            conexao.cursor.execute("UPDATE cliente SET idade = ? WHERE cpf = ?", (nova_idade, cpfPesquisar))
            print("Idade alterada com sucesso !!")
        
        elif dado_update == 'cpf':
            novo_cpf = input("Novo CPF: ")
            conexao.cursor.execute("UPDATE cliente SET cpf = ? WHERE cpf = ?", (novo_cpf, cpfPesquisar))
            print("CPF alterado com sucesso !!")
        
        elif dado_update == 'telefone':
            novo_telefone = input("Novo Telefone: ")
            conexao.cursor.execute("UPDATE cliente SET telefone = ? WHERE cpf = ?", (novo_telefone, cpfPesquisar))
            print("Telefone alterado com sucesso !!")
        
        elif dado_update == 'endereco':
            novo_endereco = input("Novo Endereço: ")
            conexao.cursor.execute("UPDATE cliente SET endereco = ? WHERE cpf = ?", (novo_endereco, cpfPesquisar))
            print("Endereço alterado com sucesso !!")
        
        elif dado_update == 'cidade':
            nova_cidade = input("Nova Cidade: ")
            conexao.cursor.execute("UPDATE cliente SET cidade = ? WHERE cpf = ?", (nova_cidade, cpfPesquisar))
            print("Cidade alterada com sucesso !!")
        
        elif dado_update == 'estado':
            novo_estado = input("Novo Estado: ")
            conexao.cursor.execute("UPDATE cliente SET estado = ? WHERE cpf = ?", (novo_estado, cpfPesquisar))
            print("Estado alterado com sucesso !!")
        
        else:
            print("Dado não encontrado.")
        
        conexao.conn.commit()
        conexao.conn.close()
    
    except sqlite3.Error as erro:
        print(f"Erro ao atualizar dados: {erro}")

