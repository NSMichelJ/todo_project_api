""""
    Author: NSMichelJ
    Github: https://github.com/NSMichelJ
    Create Date: 21/08/2021
"""

from datetime import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from .models import Project, Task
from .schema import ProjectSchema, TaskSchema
from . import db

project_schema = ProjectSchema()
task_schema = TaskSchema()

class ProjectListResource(Resource):
    def get(self):
        projects = Project.query.all()
        resp = project_schema.dump(projects, many=True)
        return resp, 200

    def post(self):
        data = request.get_json()

        try:
            todo_dict = project_schema.load(data)
        except ValidationError as err:
            return {"message": err.messages}

        title = Project.query.filter_by(title=todo_dict['title']).first()
        # Si title no es None, el proyecto ya existe
        if title is not None:
            return {"message": "The project exists"}

        todo = Project(
            title=todo_dict['title'],
            description=todo_dict['description'],
        )

        for task in todo_dict['tasks']:
            todo.tasks.append(Task(task['task']))

        db.session.add(todo)
        db.session.commit()

        resp = project_schema.dump(todo)
        return resp, 201

class ProjectByIdResource(Resource):
    def get(self, id):
        project = Project.query.get(id)
        if project is None:
            return {"message": "not found"}
        resp = project_schema.dump(project)
        return resp, 200

    def put(self, id):
        project = Project.query.get(id)
        if project is None:
            return {"message": "not found"}

        data = request.get_json()
        try:
            project_dict = project_schema.load(data, partial=True)
        except ValidationError as err:
            return {"message": err.messages}

        if 'title' in project_dict:
            title = Project.query.filter_by(title=project_dict['title']).first()
            # Si title no es None, el proyecto ya existe
            if title is not None:
                return {"messaje": f"The title {title} exists"}
            project.title = project_dict['title']

        if 'description' in project_dict:
            project.description = project_dict['description']

        if 'tasks' in project_dict:
            for task in project_dict['tasks']:
                project.tasks.append(Task(task['task']))

        project.update_at = datetime.now()
        db.session.commit()

        resp = project_schema.dump(project)
        return resp, 201

    def delete(self, id):
        project = Project.query.get(id)
        if project is None:
            return {"message": "not found"}

        db.session.delete(project)
        db.session.commit()

        return {"message": f"The project {project.title} was eliminated satisfactorily"}, 200

class TaskProjectById(Resource):
    def put(self, id):
        task = Task.query.get(id)
        if task is None:
            return {"message": "The task is not exists"}

        data = request.get_json()
        try:
            task_dict = task_schema.load(data, partial=True)
        except ValidationError as err:
            return {"message": err.messages}

        if 'task' in task_dict:
            task.task = task_dict['task']

        if 'done' in task_dict:
            task.done = task_dict['done']

        task.update_at = datetime.now()

        db.session.commit()

        resp = task_schema.dump(task)
        return resp, 201

    def delete(self, id):
        task = Task.query.get(id)
        if task is None:
            return {"message": "The task is not exists"}

        db.session.delete(task)
        db.session.commit()

        return {"message": f"The task {task.task} was eliminated satisfactorily"}, 200
