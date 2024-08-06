import connect 

def criacao_tabela():        
    try:
        global TABLE
        connect.conectar_banco()
        TABLE = "pessoas"
        connect.cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE} (nome text, idade integer, email text)")
        print(f"Tabela {TABLE} criada com sucesso!")
        connect.banco.commit()
        connect.banco.close()
    except Exception as e:
        print("Erro: ", e)

