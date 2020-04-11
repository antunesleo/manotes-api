import datetime
from src.house.services import WallService, SharingService
from src.central_files.services import ArchiveService
from src.base import domain
from src import models, config as config_module

config = config_module.get_config()


class User(domain.Entity):
    repository = models.User

    def __init__(self, db_instance=None, user_dict=None):
        super(User, self).__init__(db_instance)
        self.__notes = None
        self.__shared_notes = None

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
            note_factory = WallService.pass_me_the_note_factory()
            self.__notes = note_factory.list_for_user(user_id=self.id)
        return self.__notes

    @property
    def shared_notes(self):
        if self.__shared_notes is None:
            note_sharing_factory = SharingService.pass_me_the_note_sharing_factory()
            notes_sharing = note_sharing_factory.list_for_user(self.id)
            self.__shared_notes = [WallService.create_note_for_user(note_sharing.user_id, note_sharing.note_id)
                                  for note_sharing in notes_sharing]
        return self.__shared_notes

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
        car = cls.repository.create_from_dict(user)
        return cls.create_with_instance(car)

    def __load_db_instance(self):
        if self.db_instance is None:
            self.db_instance = self.repository.one_or_none(id=self.id)

    def create_a_note(self, note_dict):
        note_dict['user_id'] = self.id
        note_factory = WallService.pass_me_the_note_factory()
        note = note_factory.create_new(note_dict)
        return note.as_dict()

    def delete_a_note(self, id):
        note = WallService.create_note_for_user(id, self.id)
        note.delete()

    def get_a_note(self, id):
        note = WallService.create_note_for_user(id, self.id)
        return note.as_dict()

    def update_a_note(self, id, note_changes):
        note = WallService.create_note_for_user(id, self.id)
        note.update(note_changes)
        return note.as_dict()

    def update(self, payload):
        self.__load_db_instance()
        payload.pop('password', None)
        payload['update_date'] = datetime.datetime.utcnow()
        self.db_instance.update_from_dict(payload)

    def change_avatar(self, files):
        self.__load_db_instance()
        avatar_file = files['avatar']
        temp_file_path = '{}/{}-{}'.format(config.TEMP_PATH, self.id, 'avatar.png')
        avatar_file.save(temp_file_path)
        scribe = ArchiveService.create_scribe_factory_for_user(self.id)
        image_path = scribe.save(temp_file_path)
        self.db_instance.avatar_path = image_path
        self.db_instance.save_db()

    def share_a_note(self, note_id, user_id):
        note = WallService.create_note_for_user(note_id, self.id)
        note_sharing_factory = SharingService.pass_me_the_note_sharing_factory()
        note_sharing_factory.share(self.id, note.id, user_id)
        note.mark_as_shared()

    def as_dict(self, full=False):
        if full:
            # TODO: Precisa fazer teste
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
