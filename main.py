from flask import Flask, render_template, request, redirect, url_for
from db import db
from models import models

app = Flask(__name__)

@app.route("/")
def f():
    return render_template("index.html")

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        task_name = request.form.get("task_name")
        task_description = request.form.get("task_description")
        task_full_text = request.form.get("task_full_text")
        task_is_important = request.form.get("task_is_important") == 'on'
        task_status = request.form.get("task_status") == 'on'

        new_task = models.Task(id=len(db.get_all_tasks()) + 1,
                        name=task_name,
                        description=task_description,
                        full_text=task_full_text,
                        is_important=task_is_important,
                        status=task_status)
        db.new_task(new_task)

        return redirect(url_for('tasks'))

    tasks = db.get_all_tasks()
    return render_template("tasks.html", tasks=tasks)

@app.route("/create_task", methods=["GET"])
def create_task():
    return render_template("newtask.html")

if __name__ == '__main__':
    app.run(debug=True)
