from multiprocessing import cpu_count
from os import environ


def get_environment_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        return environ[var_name]
    except KeyError:
        error_msg = f'Set the environment variable {var_name}'
        raise Exception(error_msg)


class BaseConfig:
    """Base configuration"""
    CELERY_BROKER_URL = get_environment_variable('CELERY_BROKER_URL')
    CELERY_TIMEZONE = get_environment_variable('CELERY_TIMEZONE')
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': get_environment_variable('MONGODB_DB'),
        'host': get_environment_variable('MONGODB_HOST'),
        'port': int(get_environment_variable('MONGODB_PORT')),
        'username': get_environment_variable('MONGODB_USERNAME'),
        'password': get_environment_variable('MONGODB_PASSWORD'),
    }
    SWAGGER = {
        'title': get_environment_variable('SWAGGER_TITLE'),
        'uiversion': get_environment_variable('SWAGGER_UI_VERSION'),
        'openapi': get_environment_variable('SWAGGER_OPENAPI_VERSION'),
    }
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""


# Gunicorn
accesslog = '-'
bind = get_environment_variable('GUNICORN_BIND_SOCKET')
log_level = get_environment_variable('LOG_LEVEL')
max_requests = 1000
workers = 2 * cpu_count() + 1
