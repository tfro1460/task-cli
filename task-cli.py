import json, argparse, os
from datetime import datetime

class Task:
    def __init__(self, description, id=None, status="todo", createdAt=None, updatedAt=None):
        self.id = id if id is not None else len(tasks) + 1
        self.description = description
        self.status = status
        self.createdAt = createdAt if createdAt else datetime.now().isoformat()
        self.updatedAt = updatedAt if updatedAt else datetime.now().isoformat()

def add_task(args):
    tasks.append(Task(args.description))
    save_tasks()
    print(f"Task added successfully (ID: {len(tasks)})")

def update_task(args):
    try:
        tasks[args.id - 1].description = args.description
        save_tasks()
        print(f"Task updated successfully (ID: {args.id})")
    except IndexError:
        print("That id doesn't exist type 'list' to see the ids of all tasks.")

def delete_task(id):
    pass

def mark_task_in_progress(id):
    pass

def mark_task_done(id):
    pass

def list_tasks():
    pass

def save_tasks():
    tasks_dict = [vars(task) for task in tasks]
    with open('tasks.json', 'w') as f:
        json.dump(tasks_dict, f)

# Open json file and load the data
try:
    with open('tasks.json', 'r', encoding='utf-8') as f:
        tasks_dict = json.load(f)
except FileNotFoundError:
    with open('tasks.json', 'w') as f:
        tasks_dict = []
        json.dump(tasks_dict, f)

# Turns the imported dicitonary into objects
tasks = [Task(**task) for task in tasks_dict]

# Create the parser and the subparsers for the commands
parser = argparse.ArgumentParser(prog="task-cli", description="Task Tracker CLI")
subparsers = parser.add_subparsers(dest="command", required=True)

# add command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", help="A short descrtiption of the task")
add_parser.set_defaults(func=add_task)

# update command
update_parser = subparsers.add_parser("update", help="Updates the description of a task")
update_parser.add_argument("id", help="The unique identifier for the task", type=int)
update_parser.add_argument("description", help="A short description of the task")
update_parser.set_defaults(func=update_task)

# delete command
delete_parser = subparsers.add_parser("delete", help="Deletes a task")
delete_parser.add_argument("id", help="The unique identifier for the task", type=int)
delete_parser.set_defaults(func=delete_task)

# mark-in-progress command
mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Changes a task's status to in-progress")
mark_in_progress_parser.add_argument("id", help="The unique identifier for the task", type=int)
mark_in_progress_parser.set_defaults(func=mark_task_in_progress)

# mark-done command
mark_done_parser = subparsers.add_parser("mark-done")
mark_done_parser.add_argument("id", help="The unique identifier for the task", type=int)
mark_done_parser.set_defaults(func=mark_task_done)

# list command
list_parser = subparsers.add_parser("list")
list_parser.add_argument("status", nargs="?", help="The status of the task")
list_parser.set_defaults(func=list_tasks)

args = parser.parse_args()
args.func(args)