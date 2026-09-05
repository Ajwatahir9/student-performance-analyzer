import os

TODO_FILE = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\n📋 YOUR TO-DO LIST:")
        print("-" * 30)
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task '{task}' added successfully!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Task deleted: {removed}")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nEnter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = tasks[num - 1] + " ✅ DONE"
            save_tasks(tasks)
            print("✅ Task marked as done!")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n" + "=" * 30)
        print("📝 TO-DO LIST MANAGER")
        print("=" * 30)
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        print("=" * 30)
        
        choice = input("Choose option (1-5): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1-5.")

if __name__ == "__main__":
    main()