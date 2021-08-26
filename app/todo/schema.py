""""
    Author: NSMichelJ
    Github: https://github.com/NSMichelJ
    Create Date: 21/08/2021
"""

from marshmallow import fields

from .models import Project, Task
from . import ma

class ProjectSchema(ma.SQLAlchemySchema):
    """
    Schema of the Project
    """

    class Meta:
        """
        Class Meta
        """
        model = Project

    id = ma.auto_field(dump_only=True)
    title = ma.auto_field(required=True)
    description = ma.auto_field(required=True)
    created_at = ma.auto_field(dump_only=True)
    update_at = ma.auto_field(dump_only=True)
    tasks = fields.Nested('TaskSchema', many=True, required=True)


class TaskSchema(ma.SQLAlchemySchema):
    """
    Schema of the Task
    """

    class Meta:
        """
        Class Meta
        """
        model = Task
        include_fk = True

    id = ma.auto_field(dump_only=True)
    task = ma.auto_field(required=True)
    done = ma.auto_field(required=False)
    created_at = ma.auto_field(dump_only=True)
    update_at = ma.auto_field(dump_only=True)
