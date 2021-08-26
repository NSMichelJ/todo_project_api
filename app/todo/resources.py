""""
    Author: NSMichelJ
    Github: https://github.com/NSMichelJ
    Create Date: 21/08/2021
"""

from flask import Blueprint
from flask_restful import Resource, Api

from .todo import (
    ProjectListResource,
    ProjectByIdResource,
    TaskProjectById
)

api_bp = Blueprint('api_v1', __name__)

api = Api(api_bp)

class HelloWorld(Resource):
    """
    Resource Hello World
    """
    def get(self):
        """"
        Method GET
        """
        return {"message": "Hello World"}

api.add_resource(HelloWorld, '/')
api.add_resource(ProjectListResource, '/api/v1/projects/')
api.add_resource(ProjectByIdResource, '/api/v1/project/<int:id>')
api.add_resource(TaskProjectById, '/api/v1/task/<int:id>')
