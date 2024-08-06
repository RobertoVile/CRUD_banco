import sqlite3

def conectar_banco():
    global banco, cursor
    banco = sqlite3.connect('guilhermo.db')
    cursor = banco.cursor()
    print("Banco conectado com sucesso!")
    return banco, cursor