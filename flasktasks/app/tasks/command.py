import subprocess

from bson import ObjectId
from pymongo import MongoClient

from app import celery
from app.config import get_environment_variable


@celery.task(name='executor')
def executor(identifier: str):
    client = MongoClient(
        host=get_environment_variable('MONGODB_HOST'),
        port=int(get_environment_variable('MONGODB_PORT')),
        username=get_environment_variable('MONGODB_USERNAME'),
        password=get_environment_variable('MONGODB_PASSWORD'),
        authSource=get_environment_variable('MONGODB_DB'),
    )
    db = client.tasks
    task = db.task_document.find_one({'_id': ObjectId(identifier)})
    result = subprocess.check_output(task['cmd'].split())
    db.task_document.update({'_id': ObjectId(identifier)}, {"$set": {'output': result.decode('UTF-8')}}, upsert=False)
