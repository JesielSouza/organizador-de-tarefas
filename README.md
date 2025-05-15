# Organizador de Tarefas com Django 🗂️

Este é um projeto de aplicação web para gerenciamento de tarefas pessoais com autenticação de usuário, desenvolvido com Django e Bootstrap.

## 🔧 Funcionalidades

- Login e logout de usuários
- Cada usuário vê apenas suas tarefas
- Cadastro de novas tarefas
- Filtro por categoria
- Interface responsiva com Bootstrap
- Em desenvolvimento contínuo

## 🚀 Como rodar o projeto localmente

1. Clone o repositório:

```bash
git clone https://github.com/SeuUsuario/organizador-de-tarefas.git
cd organizador-de-tarefas
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode as migrações e crie o superusuário:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. Inicie o servidor:

```bash
python manage.py runserver
```

6. Acesse no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📁 Estrutura do Projeto

- `tarefas/` - App principal
- `tarefas_web/` - Configurações do Django
- `templates/` - Interface HTML com Bootstrap
- `cadastro.json` - Arquivo legado (versão terminal)
- `lista_corrigida.py` - Script legado (versão terminal)

## 📌 Observações

Este projeto nasceu como um organizador de tarefas via terminal com JSON e evoluiu para uma aplicação web usando Django. Alguns arquivos da versão anterior foram mantidos como referência.

## 📜 Licença

Este projeto está sob a licença MIT.
