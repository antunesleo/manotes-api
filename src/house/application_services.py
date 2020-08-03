from src.central_files.services import ArchiveService
from src.house.services_locator import HouseLocator
from src.models import config


class ApplicationService(object):
    pass


class NoteCreator(ApplicationService):

    def __init__(self, user):
        self.__user = user
        self.__note_factory = HouseLocator.pass_me_the_note_factory()

    def create(self, note_dict):
        note_dict['user_id'] = self.__user.id
        note = self.__note_factory.add(note_dict)
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
        self.__scribe = ArchiveService.create_scribe_factory_for_user(user.id)

    def change_avatar(self, files):
        self.__user.__load_db_instance()
        avatar_file = files['avatar']
        temp_file_path = '{}/{}-{}'.format(config.TEMP_PATH, self.__user.id, 'avatar.png')
        avatar_file.save(temp_file_path)
        image_path = self.__scribe.save(temp_file_path)
        self.__user.db_instance.avatar_path = image_path
        self.__user.db_instance.save_db()


class NoteSharer(ApplicationService):

    def __init__(self, user):
        self.__user = user
        self.__note_sharing_factory = HouseLocator.pass_me_the_note_sharing_factory()

    def share(self, note_id, user_id):
        note = HouseLocator.create_note_for_user(note_id, self.__user.id)
        self.__note_sharing_factory.share(self.__user.id, note.id, user_id)
        note.mark_as_shared()


class NoteLister(ApplicationService):

    def __init__(self, user):
        self.__user = user
        self.__note_factory = HouseLocator.pass_me_the_note_factory()

    def list(self):
        return self.__note_factory.list(user_id=self.__user.id)


class SharedNotesLister(ApplicationService):

    def __init__(self, user):
        self.__user = user
        self.__notes_sharing_factory = HouseLocator.pass_me_the_note_sharing_factory()

    def list(self, ):
        shareds = self.__notes_sharing_factory.list_for_user(self.__user.id)
        return [HouseLocator.create_note_for_user(shared.user_id, shared.note_id) for shared in shareds]
