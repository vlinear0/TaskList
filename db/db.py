import sqlite3
from models import models

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
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
    INSERT INTO tasks (id, name, description, full_text, is_important, status) VALUES (?, ?, ?, ?, ?, ?)
  ''', (task.id, task.name, task.description, task.full_text, task.is_important, task.status))
  conn.commit()


def get_all_tasks():
  cursor.execute('''
    SELECT * FROM tasks
  ''')
  rows = cursor.fetchall()
  return rows