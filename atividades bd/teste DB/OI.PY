import sqlite3

def criar_banco_e_tabela():
    try:
        # Conectar ao banco de dados (ou criar se não existir)
        conn = sqlite3.connect('exemplo.db')
        cursor = conn.cursor()
        
        # Criar a tabela
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exemplo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor TEXT
            )
        ''')
        
        # Confirmar as mudanças
        conn.commit()
        print("Banco de dados e tabela criados com sucesso.")
    
    except sqlite3.Error as e:
        print(f"Erro ao criar banco de dados ou tabela: {e}")
    
    finally:
        conn.close()

# Executar a função para criar o banco e a tabela
criar_banco_e_tabela()


import sqlite3

def inserir_valor(novo_valor):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect('exemplo.db')
        cursor = conn.cursor()
        
        # Inserir o valor
        cursor.execute('''
            INSERT INTO exemplo (valor)
            VALUES (?)
        ''', (novo_valor,))
        
        # Confirmar as mudanças
        conn.commit()
        print(f"Valor '{novo_valor}' inserido com sucesso.")
    
    except sqlite3.Error as e:
        print(f"Erro ao inserir valor: {e}")
    
    finally:
        conn.close()

# Inserir um valor de exemplo
inserir_valor('RECEBA')


import sqlite3

def atualizar_valor(id, novo_valor):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect('exemplo.db')
        cursor = conn.cursor()
        
        # Atualizar o valor
        cursor.execute('''
            UPDATE exemplo
            SET valor = ?
            WHERE id = ?
        ''', (novo_valor, id))
        
        # Confirmar as mudanças
        conn.commit()
        print(f"Valor atualizado para '{novo_valor}' com sucesso.")
    
    except sqlite3.Error as e:
        print(f"Erro ao atualizar valor: {e}")
    
    finally:
        conn.close()

# Atualizar o valor com ID 1 (certifique-se de que o ID exista no banco)
atualizar_valor(1, 'Valor Atualizado')
