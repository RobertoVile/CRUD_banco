import conexao

def criar_tabela():
    conexao.conectar_banco()
    criar_tabela = "CREATE TABLE IF NOT EXISTS cliente (nome string, sobrenome string, idade integer,cpf integer, telefone integer, endereco string, cidade string, estado string)"
    conexao.cursor.execute(criar_tabela)
    print("tabela criada")

   