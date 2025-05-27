import argparse
import json
import os

DATA_FILE = "tasks.json"

# Asegura que el archivo exista
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_tasks():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    if tasks:
        next_id = max(task.get("id", 0) for task in tasks) + 1
    else:
        next_id = 1
    tasks.append({"id": next_id, "description": description, "done": False})
    save_tasks(tasks)
    print(f"Tarea añadida con ID {next_id}.")

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        status = "✓" if task["done"] else "✗"
        print(f"{task['id']}. [{status}] {task['description']}")

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["done"] = True
            save_tasks(tasks)
            print("Tarea completada.")
            break
    else:
        print("ID inválido.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task.get("id") != task_id]
    if len(new_tasks) != len(tasks):
        save_tasks(new_tasks)
        print("Tarea eliminada.")
    else:
        print("ID inválido.")

# CLI
parser = argparse.ArgumentParser(description="Gestor de tareas")
subparsers = parser.add_subparsers(dest="command")

# Comando: add
add_parser = subparsers.add_parser("add", help="Añadir una tarea")
add_parser.add_argument("description", help="Descripción de la tarea")

# Comando: list
subparsers.add_parser("list", help="Listar tareas")

# Comando: done
done_parser = subparsers.add_parser("done", help="Marcar tarea como completada")
done_parser.add_argument("id", type=int, help="ID de la tarea")

# Comando: delete
delete_parser = subparsers.add_parser("delete", help="Eliminar una tarea")
delete_parser.add_argument("id", type=int, help="ID de la tarea")

# Ejecutar
args = parser.parse_args()

if args.command == "add":
    add_task(args.description)
elif args.command == "list":
    list_tasks()
elif args.command == "done":
    complete_task(args.id)
elif args.command == "delete":
    delete_task(args.id)
else:
    parser.print_help()
