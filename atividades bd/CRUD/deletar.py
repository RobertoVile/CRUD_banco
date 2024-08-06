import conexao
import select
import sqlite3
def deletarDado():

    conexao.conectar_banco()
       
    CPFinserido = input("Insira o CPF do cliente que deseja apagar: ")

    try:
            resultado = conexao.conn.execute('''SELECT * FROM cliente WHERE CPF = ? ''',(CPFinserido,)).fetchall()
            if(resultado == []):
                print("CPF não encontrado!")    
            else:
                conexao.cursor.execute(f"DELETE FROM cliente WHERE cpf = ?",(CPFinserido,))
                print("bora")
                print("Cliente excluído excluído com sucesso!")

    except Exception as erro:
         print("Erro ao excluir dados: ",erro)
    conexao.conn.commit()
    conexao.conn.close()

