import sqlite3
import conexao

def cadastro():
    try:
        conexao.conectar_banco()
        nome= input("Informe seu nome: ")
        sobrenome = input("Informe seu sobrenome: ")
        idade = int(input("Informe sua idade: "))
        cpf = input("Informe seu CPF: ")
        telefone = int(input("Informe seu N° de Telefone: "))
        endereco = input("Informe seu Endereço: ")
        cidade = input('Informe a cidade: ')
        estado = input("Informe o Estado: ")

        inserir_cliente ="INSERT INTO cliente VALUES('" +nome+ "', '" +sobrenome+ "', '" +str(idade)+ "', '" +str(cpf)+ "', '" + str(telefone) + "', '" + endereco + "', '" + cidade + "', '" + estado + "')"

        conexao.cursor.execute(inserir_cliente)
        conexao.conn.commit()
        conexao.conn.close()

        print("CLIENTE CADASTRADO COM SUCESSO")
        
    except sqlite3.Error as erro:
        print("Erro ao cadastrar cliente",erro)