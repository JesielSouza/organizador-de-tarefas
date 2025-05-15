import json
import bcrypt
import getpass
import lista

def salva_info(usuarios, arquivo="cadastro.json"):
    with open(arquivo, "w", encoding="utf-8") as s:
        json.dump(usuarios, s, indent=4, ensure_ascii=False)

def verifica_info(arquivo="cadastro.json"):
    try:
        with open(arquivo, "r", encoding="utf-8") as s:
            return json.load(s)
    except FileNotFoundError:
        return []
def executar():
    usuarios = verifica_info()
    while True:
        print("""\nBEM VINDO AO ORGANIZADOR DE TAREFAS\n
        1 - Acessar Organizador
        2 - Cadastrar Usuário""")
        menu = input("\nEscolha a opção desejada (ex: 2): ")   

        if menu == "2":
            cadastro_usuario = input("Cadastre seu nome de usuário: ")
            cadastro_senha = getpass.getpass("Cadastre sua senha: ")
            
            senha_crustada = bcrypt.hashpw(cadastro_senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            info = {
                "login": cadastro_usuario,
                "senha": senha_crustada
            }
            print("\nUsuário cadastrado com sucesso!")
            usuarios.append(info)
            salva_info(usuarios)
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