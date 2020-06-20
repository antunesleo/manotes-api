from src import exceptions
from src.async_tasks import tasks
from src.house import services_locator
from src.security import security_services


class Clerk(object):

    def __init__(self):
        self.__user = None
        self.__created_user = None

    @classmethod
    def create(cls):
        return cls()

    def __create_credentials(self):
        self.__user['password'] = security_services.HashService.hash(self.__user['password'])
        self.__user['token'] = security_services.TokenService.generate()

    def __validate_email(self):
        if not security_services.ValidationService.is_email(self.__user['email']):
            raise exceptions.InvalidEmail('Could not create user account because the email: {} is invalid'.format(self.__user['email']))

    def __start_to_send_confirmation_email(self):
        name = self.__created_user.username
        from_address = "antunesleo4@gmail.com"
        to_address = self.__created_user.email
        subject = "Test"
        tasks.start_send_email(name, from_address, to_address, subject)

    def create_user_account(self, user):
        self.__user = user
        self.__create_credentials()
        self.__validate_email()

        user_factory = services_locator.ResidentsService.pass_me_the_user_factory()
        self.__created_user = user_factory.create_new()

        self.__start_to_send_confirmation_email()
        return self.__created_user.as_dict()
