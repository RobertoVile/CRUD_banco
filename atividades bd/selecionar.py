import conexao
import tabela
def inserir():
    try:
        conexao.conectar_banco()
        nome = input("Qual o nome a ser inserido? ")
        idade = int(input("Qual a idade a ser inserida? "))
        email = input("Qual o email a ser inserido? ")
        conexao.cursor.execute(f"INSERT INTO {tabela.TABLE} (nome, idade, email) VALUES ('{nome}', {idade}, '{email}')")
        conexao.banco.commit()
        print("Dados inseridos com sucesso!")
        conexao.banco.close()
    except Exception as e:
        print("Erro ao inserir dados: ", e)
    