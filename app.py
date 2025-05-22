from models import db, Usuario
from flask import Flask, render_template, request, redirect, session, url_for
from app import db
import json, os
import bcrypt

app = Flask(__name__)
app.secret_key = "chave-secreta-123"  # Necessário para usar sessões

# CONFIGURAÇÃO DO BANCO SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "instance", "app.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Inicia o banco com o app
from models import db, Usuario, Tarefa
db.init_app(app)


# Utilitário: carregar usuários
def carregar_usuarios():
    try:
        with open("usuarios.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Utilitário: salvar usuários
def salvar_usuarios(usuarios):
    with open("usuarios.json", "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

# Rota de login (GET e POST)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form["login"]
        senha = request.form["senha"]
        usuario = Usuario.query.filter_by(login=login).first()
        if not usuario:
            return "Usuário não encontrado", 404

        if bcrypt.checkpw(senha.encode(), usuario.senha_hash.encode()):
            session["usuario"] = usuario.login
            return redirect("/tarefas")
        else:
            return "Senha Incorreta", 401
    return render_template("login.html")

# Rota de cadastro
@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        login = request.form["login"]
        email = request.form["email"]
        senha = request.form["senha"]

        usuario_existente = Usuario.query.filter_by(login=login).first()
        if usuario_existente:
            return "⚠️ Usuário já existe"
        
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
        
        novo_usuario = Usuario(
            login = login, 
            email = email, 
            senha_hash = senha_hash
        )

        db.session.add(novo_usuario)
        db.session.commit()

        session["usuario"] = login
        return redirect("/tarefas")
    return render_template("cadastro.html")

@app.route("/nova", methods=["GET", "POST"])
def nova_tarefa():
    if "usuario" not in session:
        return redirect("/login")

    usuario = Usuario.query.filter_by(login=session["usuario"]).first()

    if request.method == "POST":
        nome = request.form["nome"]
        prazo = request.form["prazo"]
        prioridade = request.form["prioridade"]
        categoria = request.form["categoria"]

        nova = Tarefa(
            nome=nome,
            prazo=prazo,
            prioridade=prioridade,
            categoria=categoria,
            usuario_id=usuario.id
        )

        db.session.add(nova)
        db.session.commit()

        return redirect("/tarefas")

    return render_template("nova.html")



@app.route("/tarefas")
def tarefas():
    if "usuario" not in session:
        return redirect("/login")

    usuario = Usuario.query.filter_by(login=session["usuario"]).first()
    tarefas = Tarefa.query.filter_by(usuario_id=usuario.id).all()

    return render_template("lista.html", tarefas=tarefas, usuario=usuario.login)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")



if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)