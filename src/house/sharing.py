from src import exceptions
from src import models
from src import config as config_module
from src.house import services_locator
from src.base import domain

config = config_module.get_config()


class NoteSharing(domain.Aggregate):
    active_repository = models.NoteSharing

    def __init__(self, db_instance):
        super(NoteSharing, self).__init__(db_instance)
        self.id = db_instance.id
        self._notes = None

    @classmethod
    def share(cls, giver_id, note_id, user_id):
        try:
            services_locator.HouseLocator.create_user_with_id(user_id)
        except exceptions.NotFound:
            raise exceptions.UserNotExists('Could not share note {} because the user {} does not exists'.format(user_id, note_id))

        try:
            services_locator.HouseLocator.create_note_for_user(note_id, giver_id)
        except exceptions.NotFound:
            raise exceptions.NoteNotFound('Could not share note {} because it was not found')
        except exceptions.NotMine:
            raise exceptions.NoteNotMine('Could not share note {} because it is not yours')

        sharing = {'giver_id': giver_id, 'note_id': note_id, 'user_id': user_id}
        cls.active_repository.create_from_dict(sharing)

    @classmethod
    def list_for_user(cls, user_id):
        db_instances = cls.active_repository.filter(user_id=user_id)
        return [cls.create_with_instance(db_instance) for db_instance in db_instances]
