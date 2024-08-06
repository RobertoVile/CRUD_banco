def deletar():

    import sqlite3

    try:
        banco = sqlite3.connect('primeiro_banco.db')

        cursor = banco.cursor()

        cursor.execute("DELETE from pessoas WHERE idade = 40")

        banco.commit()

        print("receba meu casca de bala")

    except sqlite3.Error as erro:
        print("Erro ao excluir: ", erro)
