import typer
from rich import print
from storage import load_tasks, save_tasks

app = typer.Typer(help="Mini-tasks CLI: Gerencie suas tarefas de forma simples e eficiente.")

@app.command(help="Adiciona uma nova tarefa")
def add():
    tasks= load_tasks()

    title = typer.prompt("Título da tarefa")
    interval = typer.prompt("Intervalo dos avisos (minutos)", type=int)
    start = typer.prompt("Horário inicial (HH:MM)")
    end = typer.prompt("Horário final (HH:MM)")

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "type": "lembrete", ## Tarefa
        "schedule": {
            "interval_minutes": interval,
            "start": start,
            "end": end,
            "days": ["mon", "tue", "wed", "thu", "fri"]
        },
        "last_run": None,
        "active": True
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("[green]Tarefa criada![/green]")

@app.command(help="Lista todas as tarefas ativas.")
def list():
    tasks = load_tasks()
    for t in tasks:
        if not t["active"]:
            continue
        print(f"[cyan]{t['id']}[/cyan] - {t['title']}")

@app.command(help="Executa o aplicativo.")
def run():
    from scheduler import run
    run()

if __name__ == "__main__":
    app()
