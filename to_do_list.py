TASKS_FILE = "tasks.txt"

# Load tasks
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            lines = f.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return []

# Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Show tasks
def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks! You’re all caught up.")
        return
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

# Add a task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append("[ ] " + title)
    save_tasks(tasks)
    print("✅ Task added.")

# Mark task as done
def mark_done(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        if not tasks[index].startswith("[X]"):
            tasks[index] = "[X]" + tasks[index][3:]
            save_tasks(tasks)
            print("✅ Task marked as done.")
        else:
            print("⚠️ Task is already marked as done.")
    else:
        print("⚠️ Invalid task number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("🗑️ Task deleted.")
    else:
        print("⚠️ Invalid task number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n📋 To-Do List Menu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
