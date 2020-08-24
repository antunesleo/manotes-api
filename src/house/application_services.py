from src.central_files.services import ArchiveService
from src.house.services_locator import HouseLocator
from src.models import config


class ApplicationService(object):
    pass


class NoteService(ApplicationService):

    def __init__(self):
        self.__note_class = HouseLocator.pass_me_the_note_class()

    def create(self, user_id, note_dict):
        note_dict['user_id'] = user_id
        note = self.__note_class.add(note_dict)
        return note.as_dict()

    def delete(self, user_id, note_id):
        note = self.__note_class.create_with_id(note_id, user_id)
        note.delete()

    def find(self, note_id, user_id):
        note = self.__note_class.create_with_id(note_id, user_id)
        return note.as_dict()

    def update(self, user_id, note_id, note_changes_dict):
        note = self.__note_class.create_with_id(note_id, user_id)
        note.update(note_changes_dict)
        return note.as_dict()

    def list(self, user_id):
        return self.__note_class.list(user_id=user_id)


class AvatarService(ApplicationService):

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
