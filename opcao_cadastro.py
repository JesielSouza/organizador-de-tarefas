import getpass
import bcrypt
import json
import os
from teste_senha import salva_info  # ← importa do seu módulo
from verificador_senha import verifica_senha
def cadastro():
    cadastro_email = input("Informe um email: ")
    cadastro_usuario = input("Informe seu nome de usuário: ")
    cadastro_senha = getpass.getpass("Cadastre sua senha: ")
    erros = verifica_senha(cadastro_senha)
    if erros:
        print("\n⚠ A senha não atende aos critérios de segurança: ")
        for erro in erros:
            print(f"- {erro}")
        return

    senha_crustada = bcrypt.hashpw(cadastro_senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    info = {
        "email": cadastro_email,
        "login": cadastro_usuario,
        "senha": senha_crustada
    }

    # Carrega os usuários
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as f:
            try:
                usuarios = json.load(f)
            except json.JSONDecodeError:
                usuarios = []
    else:
        usuarios = []

    # Verifica duplicidade
    if any(u["login"] == cadastro_usuario for u in usuarios):
        print("\n⚠️  Este nome de usuário já está cadastrado.")
        return

    usuarios.append(info)
    salva_info(usuarios)  # ← chama sua função

    print("\n✅ Usuário cadastrado com sucesso!")
