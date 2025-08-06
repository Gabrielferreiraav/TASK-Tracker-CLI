import json
import os
import uuid
import sys
import argparse

DATABASE_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as f:
            json.dump([], f)
        return []
    
    with open(DATABASE_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATABASE_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    new_task = {
        "id": str(uuid.uuid4()),
        "task": task,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarefa adicionada: {task}")

def update_task(task_id, new_task):
    tasks = load_tasks()
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = new_task
            task_found = True
            break
    if task_found:
        save_tasks(tasks)
        print(f"Tarefa atualizada: {new_task}")
    else:
        print("Tarefa não encontrada")

def delete_tasks(task_id):
    tasks = load_tasks()
    initial_count = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) < initial_count:
        save_tasks(tasks)
        print(f"Tarefa removida: {task_id}")
    else:
        print("Tarefa não encontrada")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada")
    else:
        for i, task in enumerate(tasks):
            print(f"ID: {task['id']} | Tarefa: {task['task']} | Concluida: {task['completed']}")

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas")
    subparsers = parser.add_subparsers(dest="command", help ="Comandos Disponiveis")

    parser_add = subparsers.add_parser("add", help="Adiciona uma nova tarefa")
    parser_add.add_argument("task", type=str, help="Tarefa a ser adicionada")

    parser_list = subparsers.add_parser("list", help="Lista todas as tarefas")

    parser_update = subparsers.add_parser("update", help="Atualiza uma tarefa")
    parser_update.add_argument("task_id", type =str, help="ID único da tarefa a ser atualizada")
    parser_update.add_argument("new_task", type =str, help="Nova tarefa")
    
    parser_delete = subparsers.add_parser("delete", help="Remove uma tarefa")
    parser_delete.add_argument("task_id", type =str, help="ID único da tarefa a ser removida")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "update":
        update_task(args.task_id, args.new_task)
    elif args.command == "delete":
        delete_tasks(args.task_id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
