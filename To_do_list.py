# Simple to do list whihch continue to edit and update 

import sqlite3
from datetime import datetime


# Connect to the SQLite database
conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        date TEXT,
        status TEXT DEFAULT 'pending'
    )
''')

# function for adding tasks
def add_task(task, description):
    date_added = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO tasks (title, date, description) VALUES (?,?,?)", (task, date_added, description))
    conn.commit()


#function for showing all the task 
def show_task():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]}. {row[1]}. {row[2]}. {row[3]}. {row[4]}")


# function for marking the task as done
def complete_task(task_id):
   cursor.execute(' UPDATE tasks SET status = 'complete' WHERE id = ?', (task_id,))
   conn.commit() 


def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

# Maiin loop
def main():

    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as done")
        print("4. Delete a Task")
        print("5. Exit")

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
            print("\nExiting the To-Do List. ")
            conn.close()
            break

        else:
            print(f"\nInvalid choice. Please try agin")
    
if __name__ == "__main__":
    main()

