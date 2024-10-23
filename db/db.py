import sqlite3
from models import models

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    full_text TEXT,
    is_important BOOL,
    status BOOL
  )
''')

conn.commit()


def new_task(task: models.Task):
  cursor.execute('''
    INSERT INTO tasks (name, description, full_text, is_important, status) VALUES (?, ?, ?, ?, ?)
  ''', (task.name, task.description, task.full_text, task.is_important, task.status))
  conn.commit()


def get_all_tasks():
  cursor.execute('''
    SELECT * FROM tasks
  ''')
  rows = cursor.fetchall()
  return rows

def delete_task(task_id):
    cursor.execute('''
        DELETE FROM tasks
        WHERE id = ?
    ''', (task_id,))
    conn.commit()

