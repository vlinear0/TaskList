from flask import Flask, render_template, request, redirect, url_for
from db import db
from forms import forms
from models import *
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    form = forms.TaskForm()
    if request.method == "POST" and form.validate_on_submit():
        task_name = request.form.get("task_name")
        task_description = request.form.get("task_description")
        task_full_text = request.form.get("task_full_text")
        task_is_important = 'task_is_important' in request.form
        task_status = 'task_status' in request.form

        new_task = models.Task(name=task_name,
                        description=task_description,
                        full_text=task_full_text,
                        is_important=task_is_important,
                        status=task_status)
        db.new_task(new_task)

        return redirect(url_for('tasks'))

    tasks = db.get_all_tasks()
    return render_template("tasks.html", tasks=tasks, form=form)

@app.route("/create_task", methods=["GET", "POST"])
def create_task():
    form = forms.TaskForm()
    if request.method == "POST" and form.validate_on_submit():
        task_name = form.name.data
        task_description = form.description.data
        full_text = form.full_text.data
        task_is_important = form.is_important.data
        task_status = form.status.data

        new_task = models.Task(
                        name=task_name,
                        description=task_description,
                        full_text=full_text,
                        is_important=task_is_important,
                        status=task_status)
        db.new_task(new_task)

        return redirect(url_for('tasks'))
    return render_template("newtask.html", form=form)


@app.route("/delete_task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    db.delete_task(task_id)
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    app.run(debug=True)
