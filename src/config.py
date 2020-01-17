import os
from importlib import import_module
from src import exceptions


class Config(object):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    PRODUCTION = False
    ENVIRONMENT = 'development'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    APP_BASE_URL = os.environ['APP_BASE_URL']
    PORT = os.environ['PORT']
    REDIS_URL = os.environ['REDIS_URL']
    SMTP_HOST = os.environ['SMTP_HOST']
    SMTP_PORT = os.environ['SMTP_PORT']
    SMTP_USERNAME = os.environ['SMTP_USERNAME']
    SMTP_PASSWORD = os.environ['SMTP_PASSWORD']
    FILE_STORAGE_PATH = os.environ['FILE_STORAGE_PATH']
    AVATAR_BUCKET_NAME = os.environ['AVATAR_BUCKET_NAME']
    S3_AWS_ACCESS_KEY_ID = os.environ['S3_AWS_ACCESS_KEY_ID']
    S3_AWS_SECRET_ACCESS_KEY = os.environ['S3_AWS_SECRET_ACCESS_KEY']
    TEMP_PATH = os.environ['TEMP_PATH']


class ProductionConfig(Config):
    PRODUCTION = True


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_RECORD_QUERIES = True # WTF?????


class TestingConfig(Config):
    TESTING = True
    KEY_ON_TEST = 'KEY ON TEST' # WTF????????
    ENVIRONMENT = 'test'


def get_config():
    config_imports = os.environ['APP_SETTINGS'].split('.')
    config_class_name = config_imports[-1]
    config_module = import_module('.'.join(config_imports[:-1]))
    config_class = getattr(config_module, config_class_name, None)
    if not config_class:
        raise exceptions.ConfigClassNotFound('Could not find a config class in {}'.format(os.environ['APP_SETTINGS']))
    return config_class
