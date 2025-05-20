import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.text import Text

def salvar_tarefas(tarefas, arquivo):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def carregar_tarefas(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def prioridade_valor(p):
    return {"alta": 1, "média": 2, "media": 2, "baixa": 3}.get(p.lower(), 4)

def mostrar_tarefas(tarefas, filtro=None):
    console = Console()
    table = Table(title="📝 Lista de Tarefas", header_style="bold blue")

    table.add_column("Nome", style="cyan", no_wrap=True)
    table.add_column("Prioridade", style="red")
    table.add_column("Prazo", style="green")
    table.add_column("Categoria", style="magenta")
    table.add_column("Status", style="bold yellow")

    hoje = datetime.now().date()

    for t in tarefas:
        if filtro and t["categoria"].lower() != filtro:
            continue
        
        try:
            prazo = datetime.strptime(t["prazo"], "%Y-%m-%d").date()
            status = "[bold green]✅ OK [/bold green]" if prazo >= hoje else "[bold red]⚠ VENCIDA[/bold red]"
        except:
            prazo = t["prazo"]
            status = "[yellow] ❓ Prazo inválido[/yellow]"

        table.add_row(
            t["nome"],
            t["prioridade"].capitalize(),
            str(prazo),
            t["categoria"],
            status
        )
    console.print(table)

def executar_organizador(usuario_logado):
    console = Console()
    arquivo_usuario = f"tarefas_{usuario_logado}.json"
    tarefas = carregar_tarefas(arquivo=arquivo_usuario)

    console.print(Text("Organizador de Tarefas\n", style="bold green"))
    console.print(Text("""1️⃣ - Cadastrar Tarefa\n
2️⃣ - Apagar Tarefa (temporariamente indisponível)\n
3️⃣ - Abrir lista de tarefas""", style="bold magenta"))

    selecao = Text("\n🔹 Selecione a opção desejada (ex: 2):  ", style="bold yellow")
    opcao = console.input(selecao)

    if opcao == "1":    
        while True:
            nome = input("Digite o nome da tarefa (ou 'sair' para finalizar): ")
            if nome.lower() == 'sair':
                break

            prioridade = input("Qual a prioridade? (alta / média / baixa): ")
            prazo = input("Qual o prazo? (ex: 2025-05-14): ")
            categoria = input("Categoria da Tarefa (ex: trabalho, pessoal): ")

            nova_tarefa = {
                "nome": nome,
                "prioridade": prioridade.lower(),
                "prazo": prazo,
                "categoria": categoria.lower()
            }

            tarefas.append(nova_tarefa)
            salvar_tarefas(tarefas, arquivo=arquivo_usuario)

        print("\nCadastro encerrado. Exibindo suas tarefas:")
    
    tarefas_ordenadas = sorted(tarefas, key=lambda t: prioridade_valor(t["prioridade"]))
    filtro = input("\nDeseja filtrar por categoria? (deixe em branco para não filtrar): ").lower()
    mostrar_tarefas(tarefas_ordenadas, filtro if filtro else None)
