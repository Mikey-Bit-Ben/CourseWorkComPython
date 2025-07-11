Tasks = []

def toDoList():
    print("To-Do List:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark a task as complete")
    print("4. View tasks")
    print("5. Exit")
    print()

def addTask():
    task = input("enter a task to add: ")
    Tasks.append(task)
    print(f"Task '{task}' added.")
def removeTask():
    if Tasks == []:
        print("No tasks to remove.")
        return
    #display and let the user choose a task to remove
    else:
        print("current tasks:")
        for i, task in enumerate(Tasks, start=1):
            print(f"{i}: {task}")
        choice = input("Enter the number of the task to remove: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(Tasks):
                removed_task = Tasks.pop(index)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def markComplete():
    if not Tasks:
        print("No tasks to mark as complete.")
        return
    print("Current tasks:")
    for i, task in enumerate(Tasks, start=1):
        print(f"{i}: {task}")
    try:
        index = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= index < len(Tasks):
            completed_task = Tasks[index]
            Tasks[index] = f"{completed_task} (completed)"
            print(f"Task '{completed_task}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def viewTasks():
    if not Tasks:
        print("No tasks available.")
    else:
        print("Current tasks:")
        for i, task in enumerate(Tasks, start=1):
            print(f"{i}: {task}")
def exitProgram():
    print("Exiting the program. Goodbye!")
    return False

def main():
    while True:
        toDoList()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            addTask()
        elif choice == '2':
            removeTask()
        elif choice == '3':
            markComplete()
        elif choice == '4':
            viewTasks()
        elif choice == '5':
            if not exitProgram():
                break
        else:
            print("Invalid choice. Please try again.")
        print()  

if __name__ == "__main__":
    main()
        