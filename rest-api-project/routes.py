from app import app,db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
import forms
from datetime import datetime, timezone

@app.route('/')
@app.route('/index')
def index():
    with app.app_context():
        tasks=Task.query.all()
    return render_template('index.html', tasks=tasks)
@app.route('/add' ,methods=['GET','POST'])
def add():
    form=forms.addtaskform()
    if form.validate_on_submit():
    
        t=Task(title=form.title.data, date=datetime.now(timezone.utc))
        with app.app_context():
            db.session.add(t)
            db.session.commit()

        return redirect(url_for('index'))
    return render_template('add.html',form=form)

@app.route("/edit/<int:task_id>" ,methods=["GET", "POST"])
def edit(task_id):
    task=Task.query.get(task_id)
    form=forms.addtaskform()
    if task:
        if form.validate_on_submit():
            task.title=form.title.data
            task.date=datetime.now(timezone.utc)
            db.session.commit()
            flash("task is updated")
            return redirect(url_for("index"))

        form.title.data=task.title
        return render_template("edit.html",form=form, task_id=task_id)
    flash("task not found")
    return redirect(url_for('index'))
    
@app.route("/delete/<int:task_id>" ,methods=["GET", "POST"])
def delete(task_id):
    task=Task.query.get(task_id)
    form=forms.deletetaskform()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("task is deleted")
            return redirect(url_for("index"))

        return render_template("delete.html",form=form, task_id=task_id, title=task.title)
    flash("task not found")
    return redirect(url_for('index'))
        