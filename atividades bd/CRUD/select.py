import conexao
import sqlite3

global cpf
def exibirCliente():
    conexao.conectar_banco()
    resultado = conexao.cursor.execute("SELECT * FROM cliente").fetchall()
    for result in resultado:
        print("#################################")
        print("Nome: ",result[0])
        print("Sobrenome: ",result[1])
        print("Idade: ",result[2])
        print("CPF: ",result[3])
        print("Telefone: ",result[4])
        print("Endereco: ",result[5])
        print("Cidade: ",result[6])
        print("Estado: ",result[7])
    conexao.conn.close

def consultar_CPF():
    conexao.conectar_banco()
    cpf = input("Informe o CPF que deseja consultar: ")
    try:
        resultado = conexao.conn.execute('''SELECT * FROM cliente WHERE CPF = ? ''',(cpf,)).fetchall()
        if(resultado == []):
            print("CPF não encontrado!")
        else:
            for result in resultado:
                print("#################################")
                print("Nome: ",result[0])
                print("Sobrenome: ",result[1])
                print("Idade: ",result[2])
                print("CPF: ",result[3])
                print("Telefone: ",result[4])
                print("Endereco: ",result[5])
                print("Cidade: ",result[6])
                print("Estado: ",result[7])
        return cpf
    except sqlite3.Error as erro:
        print("Erro ao encontrar cliente", erro)

