# Organizador de Tarefas com Flask 🗂️

Este é um projeto de aplicação web para gerenciamento de tarefas pessoais com autenticação de usuário, desenvolvido com **Flask**, **Bootstrap** e persistência em **JSON**.

## 🔧 Funcionalidades

- Cadastro e login de usuários com senha criptografada (bcrypt)
- Cada usuário tem seu próprio arquivo de tarefas
- Cadastro de novas tarefas com formulário
- Visualização de tarefas por usuário
- Logout de sessão
- Interface moderna com Bootstrap
- Em constante evolução

## 🚀 Como rodar o projeto localmente

1. Clone o repositório:

```bash
git clone https://github.com/JesielSouza/organizador-de-tarefas.git
cd organizador-de-tarefas
```

2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o servidor Flask:

```bash
python app.py
```

5. Acesse no navegador:

```
http://localhost:5000
```

## 📁 Estrutura do Projeto

- `app.py` — Arquivo principal com as rotas Flask
- `usuarios.json` — Armazena os usuários cadastrados
- `tarefas_<usuario>.json` — Arquivo separado por usuário
- `templates/` — Contém os arquivos HTML (login, cadastro, nova tarefa, lista)

## 📌 Observações

Este projeto começou como uma aplicação em terminal e evoluiu para um sistema web simples e funcional usando Flask e Bootstrap.

## 📜 Licença

Este projeto está sob a licença MIT.
