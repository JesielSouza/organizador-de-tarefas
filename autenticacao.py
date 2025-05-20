import bcrypt
import getpass
from opcao_cadastro import cadastro
from teste_senha import verifica_info

def executar():
    usuarios = verifica_info()
    while True:
        print("""\nBEM VINDO AO ORGANIZADOR DE TAREFAS\n
        1 - Acessar Organizador
        2 - Cadastrar Usuário""")
        menu = input("\nEscolha a opção desejada (ex: 2): ")   

        if menu == "2":
            cadastro()
            usuarios = verifica_info()  
        elif menu == "1":
            break
        else:
            print("Opção inválida. Tente novamente.")
    while True:
        usuario = input("LOGIN: ")
        senha = getpass.getpass("SENHA: ")

        for credencial in usuarios:
            if credencial["login"] == usuario:
                if bcrypt.checkpw(senha.encode('utf-8'), credencial["senha"].encode('utf-8')):
                    print(f"Acesso concedido para: {usuario}")
                    import lista
                    lista.executar_organizador(usuario)
                    exit()
        print("Usuário ou Senha incorreto!")