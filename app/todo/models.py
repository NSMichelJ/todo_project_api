""""
    Author: NSMichelJ
    Github: https://github.com/NSMichelJ
    Create Date: 21/08/2021
"""

from datetime import datetime

from . import db

class Project(db.Model):
    """
    Model of the Project
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.now())
    update_at = db.Column(db.DateTime, nullable=True, default=datetime.now())
    tasks = db.relationship('Task', backref='project', lazy=True, cascade='all, delete-orphan')

    def __init__(self, title, description, tasks=[]):
        self.title = title
        self.description = description
        self.tasks = tasks

    def __repr__(self):
        return f'Project {self.title}'

    def __str__(self):
        return f'{self.title}'

class Task(db.Model):
    """"
    Model of the Task
    """
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String, nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.now())
    update_at = db.Column(db.DateTime, nullable=True, default=datetime.now())
    project_id = db.Column(
        db.Integer,
        db.ForeignKey('project.id'),
        nullable=False
    )

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return f'Task ({self.task})'

    def __str__(self):
        return f'{self.task}'
