import connect
import create_tabela
def inserir():
    try:
        connect.conectar_banco()
        nome = input("Qual o nome a ser inserido? ")
        idade = int(input("Qual a idade a ser inserida? "))
        email = input("Qual o email a ser inserido? ")
        connect.cursor.execute(f"INSERT INTO {create_tabela.TABLE} (nome, idade, email) VALUES ('{nome}', {idade}, '{email}')")
        connect.banco.commit()
        print("Dados inseridos com sucesso!")
        connect.banco.close()
    except Exception as e:
        print("Erro ao inserir dados: ", e)
    