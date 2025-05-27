import argparse
import json
import os
from datetime import datetime

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
    now = datetime.now().isoformat()
    tasks.append({
        "id": next_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    })
    save_tasks(tasks)
    print(f"Tarea añadida con ID {next_id}.")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    for task in tasks:
        if filter_status and task.get("status") != filter_status:
            continue
        status = task.get("status", "todo")
        print(f"{task['id']}. [{status}] {task['description']} (Creada: {task.get('createdAt', '-')}, Actualizada: {task.get('updatedAt', '-')})")

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Tarea marcada como completada.")
            break
    else:
        print("ID inválido.")

def mark_in_progress_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Tarea marcada como en progreso.")
            break
    else:
        print("ID inválido.")

def mark_done_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Tarea marcada como completada.")
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

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Tarea actualizada.")
            break
    else:
        print("ID inválido.")

# CLI
parser = argparse.ArgumentParser(description="Gestor de tareas")
subparsers = parser.add_subparsers(dest="command")

# Comando: add
add_parser = subparsers.add_parser("add", help="Añadir una tarea")
add_parser.add_argument("description", help="Descripción de la tarea")

# Comando: list
list_parser = subparsers.add_parser("list", help="Listar tareas")
list_parser.add_argument("filter", nargs="?", choices=["done", "todo", "in-progress"], help="Filtrar tareas por estado")

# Comando: done
done_parser = subparsers.add_parser("done", help="Marcar tarea como completada")
done_parser.add_argument("id", type=int, help="ID de la tarea")

# Comando: delete
delete_parser = subparsers.add_parser("delete", help="Eliminar una tarea")
delete_parser.add_argument("id", type=int, help="ID de la tarea")

# Comando: update
update_parser = subparsers.add_parser("update", help="Actualizar una tarea")
update_parser.add_argument("id", type=int, help="ID de la tarea")
update_parser.add_argument("description", help="Nueva descripción de la tarea")

# Comando: mark-in-progress
mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Marcar tarea como en progreso")
mark_in_progress_parser.add_argument("id", type=int, help="ID de la tarea")

# Comando: mark-done
mark_done_parser = subparsers.add_parser("mark-done", help="Marcar tarea como completada")
mark_done_parser.add_argument("id", type=int, help="ID de la tarea")

# Ejecutar
args = parser.parse_args()

if args.command == "add":
    add_task(args.description)
elif args.command == "list":
    list_tasks(args.filter)
elif args.command == "done":
    complete_task(args.id)
elif args.command == "delete":
    delete_task(args.id)
elif args.command == "update":
    update_task(args.id, args.description)
elif args.command == "mark-in-progress":
    mark_in_progress_task(args.id)
elif args.command == "mark-done":
    mark_done_task(args.id)
else:
    parser.print_help()
