import json, argparse
from datetime import datetime
from tabulate import tabulate

def add_task(args, tasks):
    # Add a new task and save it to the json file before printing a success message
    tasks.append({
        "id": len(tasks) + 1,
        "description": args.description,
        "status": "todo",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
        })
    save_tasks(tasks)
    print_task([tasks[len(tasks) - 1]])

def update_task(args, tasks):
    # Changes the description for a task, saves it to the json file before printing a success or fail message.
    try:
        tasks[args.id - 1]["description"] = args.description
        tasks[args.id - 1]["updated_at"] = datetime.now().isoformat()
        save_tasks(tasks)
        print_task([tasks[args.id - 1]])
    except IndexError:
        print("That id doesn't exist type 'list' to see the ids of all tasks.")

def delete_task(args, tasks):
    # Delete a task, updates the ids, save it to the json and print a success or fail message.
    try:
        tasks.remove(tasks[args.id - 1])
        print_task([tasks[args.id - 1]])
        update_ids(tasks)
        save_tasks(tasks)
        print("Some ids may have changed, use the 'list' command to view changes.")
    except IndexError:
        print("That id doesn't exist type 'list' to see the ids of all tasks.")

def mark_task_in_progress(args, tasks):
    # Changes the status to in-progress for a task, saves it to the json file before printing a success or fail message.
    try:
        tasks[args.id - 1]["status"] = "in-progress"
        save_tasks(tasks)
        print_task([tasks[args.id - 1]])
    except IndexError:
        print("That id doesn't exist type 'list' to see the ids of all tasks.")    

def mark_task_done(args, tasks):
    # Changes the status to in-progress for a task, saves it to the json file before printing a success or fail message.
    try:
        tasks[args.id - 1]["status"] = "done"
        save_tasks(tasks)
        print_task([tasks[args.id - 1]])
    except IndexError:
        print("That id doesn't exist type 'list' to see the ids of all tasks.")    

def list_tasks(args, tasks):
    # Loops through all of the tasks in the array and prints them out into the terminal.
    if args.status:
        filtered_tasks = [task for task in tasks if task["status"] == args.status]
        print_task(filtered_tasks)
    else:
        print_task(tasks)
           

def save_tasks(tasks):
    # Saves the edited tasks to the json file.
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def update_ids(tasks):
    # Updates the ids by looping through all the tasks and reassigning the id variable for each one
    for i in range(len(tasks)):
        tasks[i]["id"] = i + 1

def print_task(tasks):
     print(tabulate(tasks, headers="keys", tablefmt="fancy_grid"))

def main():
    
    # Open json file and load the data
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        with open('tasks.json', 'w') as f:
            tasks = []
            json.dump(tasks, f)

    # Create the parser and the subparsers for the commands
    parser = argparse.ArgumentParser(prog="task-cli", description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="A short descrtiption of the task")
    add_parser.set_defaults(func= lambda args: add_task(args, tasks=tasks))

    # update command
    update_parser = subparsers.add_parser("update", help="Updates the description of a task")
    update_parser.add_argument("id", help="The unique identifier for the task", type=int)
    update_parser.add_argument("description", help="A short description of the task")
    update_parser.set_defaults(func= lambda args: update_task(args, tasks=tasks))

    # delete command
    delete_parser = subparsers.add_parser("delete", help="Deletes a task")
    delete_parser.add_argument("id", help="The unique identifier for the task", type=int)
    delete_parser.set_defaults(func= lambda args: delete_task(args, tasks=tasks))

    # mark-in-progress command
    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Changes a task's status to in-progress")
    mark_in_progress_parser.add_argument("id", help="The unique identifier for the task", type=int)
    mark_in_progress_parser.set_defaults(func= lambda args: mark_task_in_progress(args, tasks=tasks))

    # mark-done command
    mark_done_parser = subparsers.add_parser("mark-done", help="Changes a task's status to done")
    mark_done_parser.add_argument("id", help="The unique identifier for the task", type=int)
    mark_done_parser.set_defaults(func= lambda args: mark_task_done(args, tasks=tasks))

    # list command
    list_parser = subparsers.add_parser("list", help="Lists all tasks, optionally filtered by status")
    list_parser.add_argument("status", nargs="?", help="The status of the task")
    list_parser.set_defaults(func= lambda args: list_tasks(args, tasks=tasks))

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()