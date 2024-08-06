import connect

def deletar():
    try:
        connect.conectar_banco()
        opcaoDeletar = input("O que você quer deletar? 1 - para nome, 2 - para idade, 3 - para email: ")
        
        if opcaoDeletar == '1':
            DelNome = input("Qual o nome a ser excluído? ")
            connect.cursor.execute(f"DELETE FROM pessoas WHERE nome = '{DelNome}'")
        elif opcaoDeletar == '2':
            DelIdade = int(input("Qual a idade a ser excluída? "))
            connect.cursor.execute(f"DELETE FROM pessoas WHERE idade = {DelIdade}")
        elif opcaoDeletar == '3':
            DelEmail = input("Qual o email a ser excluído? ")
            connect.cursor.execute(f"DELETE FROM pessoas WHERE email = '{DelEmail}'")
        else:
            print("Opção inválida")
            return
        
        if connect.cursor.rowcount > 0:
            print("Dado excluído com sucesso!")
        else:
            print("Nenhum dado encontrado com os valores fornecidos.")
        
        connect.banco.commit()
    except Exception as e:
        print("Erro ao excluir dados: ", e)
    finally:
        connect.banco.close()
