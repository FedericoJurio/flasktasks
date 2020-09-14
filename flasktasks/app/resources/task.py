from typing import Tuple

from flasgger import swag_from
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError as MarshmallowValidationError
from mongoengine import ValidationError as MongoValidationError

from app.documents.task import TaskDocument
from app.schemas.task import TaskInstanceSchema, TaskListSchema
from app.tasks.command import executor


class TaskInstanceHandler(Resource):
    @swag_from('docs/get_task.yaml')
    def get(self, identifier: str) -> Tuple[dict, int]:
        try:
            task = TaskDocument.objects(id=identifier).first()
        except MongoValidationError:
            return {'message': f'Invalid identifier'}, 400

        if not task:
            return {'message': f'Task {identifier} does not exist'}, 404

        return TaskInstanceSchema().dump(task), 200


class TaskListHandler(Resource):
    @swag_from('docs/create_task.yaml')
    def post(self) -> Tuple[dict, int]:
        try:
            payload = TaskListSchema().loads(request.get_data())
        except MarshmallowValidationError as err:
            return err.messages, 422

        task = TaskDocument(cmd=payload['cmd'])
        task.save()
        executor.delay(identifier=str(task.id))

        return TaskListSchema().dump(task), 201
