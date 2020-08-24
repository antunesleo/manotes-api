import datetime

from src.house.application_services import AvatarService, NoteService
from src.base.domain import Actor, Aggregate
from src import models, config as config_module

config = config_module.get_config()


class User(Actor, Aggregate):
    active_repository = models.User

    def __init__(self, db_instance=None, user_dict=None):
        super(User, self).__init__(db_instance)
        self.__notes = None

        if db_instance:
            self.id = db_instance.id
            self.__token = None
            self.__password = None
            self.__username = None
            self.__email = None
            self.__avatar_path = None
        if user_dict:
            self.id = user_dict['id']
            self.__token = user_dict['token']
            self.__password = user_dict['password']
            self.__username = user_dict['username']
            self.__email = user_dict['email']
            self.__avatar_path = user_dict['avatar_path']

    @property
    def notes(self):
        if self.__notes is None:
            note_service = NoteService()
            self.__notes = note_service.list(self.id)
        return self.__notes

    @property
    def token(self):
        if self.__token is None:
            self.__token = self.db_instance.token
        return self.__token

    @property
    def password(self):
        if self.__password is None:
            self.__password = self.db_instance.password
        return self.__password

    @property
    def username(self):
        if self.__username is None:
            self.__username = self.db_instance.username
        return self.__username

    @property
    def email(self):
        if self.__email is None:
            self.__email = self.db_instance.email
        return self.__email

    @property
    def avatar_path(self):
        if self.__avatar_path is None:
            self.__avatar_path = self.db_instance.avatar_path
        return self.__avatar_path

    @classmethod
    def create_with_token(cls, token):
        return cls._create_with_keys(token=token)

    @classmethod
    def create_with_username(cls, username):
        return cls._create_with_keys(username=username)

    @classmethod
    def create_with_email(cls, email):
        return cls._create_with_keys(email=email)

    @classmethod
    def create_with_dict(cls, user_dict):
        return cls(user_dict=user_dict)

    @classmethod
    def create_new(cls, user):
        car = cls.active_repository.create_from_dict(user)
        return cls.create_with_instance(car)

    def load_db_instance(self):
        if self.db_instance is None:
            self.db_instance = self.active_repository.one_or_none(id=self.id)

    def create_a_note(self, note_dict):
        note_service = NoteService()
        return note_service.create(self.id, note_dict)

    def delete_a_note(self, note_id):
        note_service = NoteService()
        note_service.delete(self.id,note_id)

    def get_a_note(self, note_id):
        note_service = NoteService()
        return note_service.find(self.id, note_id)

    def update_a_note(self, note_id, note_changes_dict):
        note_service = NoteService()
        return note_service.update(self.id, note_id, note_changes_dict)

    def update(self, payload):
        self.load_db_instance()
        payload.pop('password', None)
        payload['update_date'] = datetime.datetime.utcnow()
        self.db_instance.update_from_dict(payload)

    def change_avatar(self, files):
        avatar_service = AvatarService(self)
        avatar_service.change_avatar(files)

    def as_dict(self, full=False):
        if full:
            return {
                "id": self.id,
                "username": self.username,
                "email": self.email,
                "token": self.token,
                "password": self.password,
                "avatar_path": self.avatar_path
            }
        return {
            "username": self.username,
            "email": self.email
        }
