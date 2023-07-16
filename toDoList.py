# ToDo List Application

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(str(index+1) +".", task)

def delete_task():
    view_tasks()
    if not tasks:
        return
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(deleted_task, "deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n==== ToDo List ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        print("====================")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Ending task manager.")
            break
        else:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()
