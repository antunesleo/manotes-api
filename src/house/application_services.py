from src.central_files.services import ArchiveService
from src.house.services_locator import HouseLocator
from src.models import config


class ApplicationService(object):
    pass


class NoteCreator(ApplicationService):

    def __init__(self, user):
        self.__user = user
        self.__note_class = HouseLocator.pass_me_the_note_class()

    def create(self, note_dict):
        note_dict['user_id'] = self.__user.id
        note = self.__note_class.add(note_dict)
        return note.as_dict()


class NoteDeleter(ApplicationService):

    def __init__(self, user):
        self.__user = user

    def delete(self, note_id):
        note = HouseLocator.create_note_for_user(note_id, self.__user.id)
        note.delete()


class NoteFinder(ApplicationService):

    def __init__(self, user):
        self.__user = user

    def find(self, note_id):
        note = HouseLocator.create_note_for_user(note_id, self.__user.id)
        return note.as_dict()


class NoteUpdater(ApplicationService):

    def __init__(self, user):
        self.__user = user

    def update(self, note_id, note_changes_dict):
        note = HouseLocator.create_note_for_user(note_id, self.__user.id)
        note.update(note_changes_dict)
        return note.as_dict()


class AvatarChanger(ApplicationService):

    def __init__(self, user):
        self.__user = user
        self.__scribe = ArchiveService.create_scribe_class_for_user(user.id)

    def change_avatar(self, files):
        self.__user.load_db_instance()
        avatar_file = files['avatar']
        temp_file_path = '{}/{}-{}'.format(config.TEMP_PATH, self.__user.id, 'avatar.png')
        avatar_file.save(temp_file_path)
        image_path = self.__scribe.save(temp_file_path)
        self.__user.db_instance.avatar_path = image_path
        self.__user.db_instance.save_db()


class NoteLister(ApplicationService):

    def __init__(self, user):
        self.__user = user
        self.__note_class = HouseLocator.pass_me_the_note_class()

    def list(self):
        return self.__note_class.list(user_id=self.__user.id)
