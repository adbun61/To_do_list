# Import specific functions from the database file
from todo_app.database import initialize_db, add_task, show_task, complete_task, incomplete_task, edit_task, delete_task, delete_complete, close_app



# Maiin loop
def main():
    initialize_db()
    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as done")
        print("4. Mark Task as incomplete")
        print("5. Delete a Task")
        print("6. Delete all completed tasks")
        print("7. Edit Task")
        print("0. Exit")

        choice = input(" Enter your choice: ")

        if choice == '1':
            task = input("Please enter the task you would like to add: ")
            description = input("Please enter a description: ")
            add_task(task, description)

    
        elif choice == '2':
            show_task()

        elif choice == '3':
            try:
                task_id = int(input("Enter task ID: "))
                complete_task(task_id)
            except ValueError:
                    print("Invalid task ID. Must be a number.")


        elif choice == '4':
            try:
                task_id = int(input("Enter task ID: "))
                incomplete_task(task_id)
            except ValueError:
                    print("Invalid task ID. Must be a number.")

        elif choice == '5':
            task_id = input("What task ID do you want to delete? ")
            delete_task(task_id)

        elif choice == '6':
             delete_complete()


        elif choice == '7':
            try:
                task_id = int(input("What task would you like to edit: "))
                description = input("New description: ")
                edit_task(task_id, description)
            except ValueError:
                    print("Invalid task ID. Must be a number.")
    
        elif choice == '0':
            print("\nExiting the To-Do List. ")
            close_app()
            print("\nHave a lovely day. ")
            break

        else:
            print(f"\nInvalid choice. Please try agin")
    
if __name__ == "__main__":
    main()

