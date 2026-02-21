# Import specific functions from the database file
from todo_app.database import initialize_db, add_task, show_task, complete_task, edit_task, delete_task, close_app



# Maiin loop
def main():
    initialize_db()
    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as done")
        print("4. Delete a Task")
        print("5. Edit Task")
        print("6. Exit")

        choice = input(" Enter your choice: ")

        if choice == '1':
            task = input("Please enter the task you would like to add: ")
            while True:
                add_description = input("Would you like to add a description? ")
                if add_description == "yes":
                    description = input("Please enter a description: ")
                    break
                elif add_description == "no":
                    description = "N/A"
                    break
                else:
                    print(f"incorrect choice please try again ")

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
            task_id = input("What task ID do you want to delete? ")
            delete_task(task_id)

        elif choice == '5':
            try:
                task_id = int(input("What task would you like to edit: "))
                description = input("New description: ")
                edit_task(task_id, description)
            except ValueError:
                    print("Invalid task ID. Must be a number.")


    
        elif choice == '6':
            print("\nExiting the To-Do List. ")
            close_app()
            print("\nHave a lovely day. ")
            break

        else:
            print(f"\nInvalid choice. Please try agin")
    
if __name__ == "__main__":
    main()

