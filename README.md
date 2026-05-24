# task-cli
task-cli is a simple command line interface for tracking and managing tasks. With task-cli you can seemlessly track what you need to do, what you have done and what you are currently working on.

## Installation
You can use the package manager pip to istall task-cli directly from your terminal.

```bash
pip install git+https://github.com/tfro1460/task-cli.git
```

## Usage
The list of the commands and their usage is given below:
```bash
# Adding a new task
task-cli add "Buy groceries"

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

