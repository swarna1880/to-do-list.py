# todo.py
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file into a list"""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.reaslines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks from the list into the life"""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do Lisy:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    """add a new task"""
    task = input("Enter the new task:  ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.\n")
    else:
        print("Task cannot be empty.\n")

def remove_task(tasks):
    """Remove a task by its number"""
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed task: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def show_menu():
    print("====To-Do List App ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("===================")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-4):  ").strip()
        print()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Have a Goodday!, Goodbye!")
            break
        else:
            print("Invalid option. Please try again. \n")

if __name__ == "__main__":
    main()