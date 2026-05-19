import time
from datetime import datetime
from storage import load_tasks, save_tasks
from notifier import notify

def should_run(task, now: datetime):
    if task["type"] != "recorrente":
        return False

    start = datetime.strptime(task["schedule"]["start"], "%H:%M").time()
    end = datetime.strptime(task["schedule"]["end"], "%H:%M").time()

    if not (start <= now.time() <= end):
        return False

    if task["last_run"]:
        last_run = datetime.fromisoformat(task["last_run"])
        diff = (now - last_run).total_seconds() / 60
        return diff >= task["schedule"]["interval_minutes"]

    return True


def run():
    print("Scheduler iniciado...")
    while True:
        tasks = load_tasks()
        now = datetime.now()

        for task in tasks:
            if not task["active"]:
                continue

            if should_run(task, now):
                notify(title=task["title"])
                task["last_run"] = now.isoformat()

        save_tasks(tasks)
        time.sleep(60)
