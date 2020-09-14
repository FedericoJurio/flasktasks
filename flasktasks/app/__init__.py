from apispec_webframeworks.flask import FlaskPlugin
from celery import Celery
from flasgger import APISpec, Swagger
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api

from app.config import get_environment_variable


api = Api()
celery = Celery(__name__, include=['app.tasks.command'])
mongodb = MongoEngine()
swagger = Swagger()


def create_app(app_settings: str = None) -> Flask:
    app = Flask(__name__)
    app_settings = app_settings if app_settings else get_environment_variable('APP_SETTINGS')
    app.config.from_object(app_settings)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app: Flask) -> None:
    api.init_app(app)
    mongodb.init_app(app)
    swagger.init_app(app)
    spec = APISpec(
        title=app.config['SWAGGER']['title'],
        version='1.0.0',
        openapi_version=app.config['SWAGGER']['openapi'],
        plugins=[FlaskPlugin()],
    )
    swagger.template = spec.to_flasgger(app)


def register_resources(app: Flask) -> None:
    from app.resources.task import TaskInstanceHandler, TaskListHandler
    api.add_resource(TaskInstanceHandler, '/get_output/<string:identifier>')
    api.add_resource(TaskListHandler, '/new_task')
    api.init_app(app)
