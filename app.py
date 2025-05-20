from flask import Flask, request, jsonify
import json, bcrypt, string


app = Flask(__name__)
#Funcões Auxiliares (serão reutilizadas no código)
def salvar_tarefas(tarefas, arquivo):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def carregar_tarefas(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def verificar_senha(senha_digitada, senha_hash):
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_hash.encode('utf-8'))
def verifica_senha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("Senha muito curta (mínimo 8 caracteres).")
    if not any(c.isupper() for c in senha):
        erros.append("Adicione pelo menos uma letra MAIÚSCULA.")
    if not any(c.islower() for c in senha):
        erros.append("Adicione pelo menos uma letra minúscula")
    if not any(c.isdigit() for c in senha):
        erros.append("Adicione pelo menos um número")
    if not any(c in string.punctuation for c in senha):
        erros.append("Adicione pelo menos um caractere especial (Ex: !, @, #...).")
    if any(c.isspace() for c in senha):
        erros.append("A senha não pode conter espaços.")
    
    if not erros:
        print("✅Senha válida!")
        return True
    else:
        print("Senha inválida por esses motivos: ")
        for erro in erros:
            print(erro)
        return False

app.run(debug=True)