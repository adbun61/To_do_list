import sqlite3
from datetime import datetime


# Connect to the SQLite database
conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()

def initialize_db():
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
   cursor.execute("UPDATE tasks SET status = 'complete' WHERE id = ?", (task_id,))
   conn.commit() 

# function for marking the task as not done
def incomplete_task(task_id):
   cursor.execute("UPDATE tasks SET status = 'pending' WHERE id = ?", (task_id,))
   conn.commit() 


#function for editing the task descprtion
def edit_task(task_id, description):
    cursor.execute("UPDATE tasks SET description = ? where id = ?", (description, task_id))
    conn.commit()                   

#function for deleting all completed tasks
def delete_complete():
    cursor.execute("DELETE FROM tasks WHERE status = 'complete'")
    conn.commit()

#function for deleting tasks
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

#function for closing the database
def close_app():
    conn.close()