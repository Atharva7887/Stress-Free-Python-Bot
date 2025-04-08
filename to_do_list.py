import json
import os
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

TASKS_FILE = "tasks.json"

# Load existing tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
            # Ensure old tasks get new fields if missing
            for task in tasks:
                if "priority" not in task:
                    task["priority"] = "Low"
                if "due_date" not in task:
                    task["due_date"] = "N/A"
            return tasks
    return []

# Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Show tasks with color and details
def show_tasks(tasks):
    if not tasks:
        print(Fore.GREEN + "✅ No tasks! You’re all done.")
        return

    print(Fore.CYAN + "\nYour To-Do List:")
    for i, task in enumerate(tasks):
        status = Fore.GREEN + "✅" if task["done"] else Fore.RED + "❌"
        priority_color = {
            "Low": Fore.BLUE,
            "Medium": Fore.YELLOW,
            "High": Fore.RED
        }.get(task["priority"], Fore.WHITE)

        due = task["due_date"] if task["due_date"] else "N/A"
        print(f"{i+1}. {Style.BRIGHT}{task['title']} [{status}]")
        print(f"   📅 Due: {due} | 🔥 Priority: {priority_color + task['priority']}{Style.RESET_ALL}")

# Add a task
def add_task(tasks):
    title = input("Enter task title: ")
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    priority = input("Enter priority (Low, Medium, High): ").capitalize()

    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print(Fore.RED + "⚠️ Invalid date format. Setting as N/A.")
            due_date = "N/A"

    if priority not in ["Low", "Medium", "High"]:
        print(Fore.RED + "⚠️ Invalid priority. Setting as 'Low'.")
        priority = "Low"

    tasks.append({
        "title": title,
        "done": False,
        "due_date": due_date,
        "priority": priority
    })
    save_tasks(tasks)
    print(Fore.GREEN + "✅ Task added successfully.")

# Mark a task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print(Fore.GREEN + "✅ Task marked as done.")
        else:
            print(Fore.RED + "⚠️ Invalid task number.")
    except ValueError:
        print(Fore.RED + "⚠️ Please enter a number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(Fore.YELLOW + f"🗑️ Task '{removed['title']}' deleted.")
        else:
            print(Fore.RED + "⚠️ Invalid task number.")
    except ValueError:
        print(Fore.RED + "⚠️ Please enter a number.")

# Sort tasks
def sort_tasks(tasks):
    print("\nSort by:")
    print("1. Priority")
    print("2. Due Date")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        tasks.sort(key=lambda x: ["Low", "Medium", "High"].index(x["priority"]))
    elif choice == "2":
        tasks.sort(key=lambda x: x["due_date"] if x["due_date"] != "N/A" else "9999-12-31")
    else:
        print(Fore.RED + "⚠️ Invalid choice.")
    save_tasks(tasks)
    print(Fore.GREEN + "✅ Tasks sorted.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n📋 " + Fore.CYAN + "To-Do List Menu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Sort tasks")
        print("6. Exit")

        choice = input(Fore.MAGENTA + "Enter your choice (1-6): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            sort_tasks(tasks)
        elif choice == "6":
            print(Fore.GREEN + "👋 Goodbye!")
            break
        else:
            print(Fore.RED + "⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
