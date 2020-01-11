from src.async_tasks import establish
from src.mail import postman


def start_send_email(name, from_address, to_address, subject):
    establish.logger.info('STARTING SEND EMAIL')
    task = send_email.apply_async((name, from_address, to_address, subject, ))
    return task.id


@establish.worker.task
def send_email(name, from_address, to_address, subject):
    postman.Postman.send_confirmation_email(name, from_address, to_address, subject)
