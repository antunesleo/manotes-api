from celery import Celery
from celery.utils.log import get_task_logger
from src import config as config_module

config = config_module.get_config()

logger = get_task_logger(__name__)

worker = None


def make_worker(web_app):
    global worker
    worker = Celery(web_app.import_name, broker=config.REDIS_URL)


def register_tasks(worker):
   from src.async_tasks import tasks
