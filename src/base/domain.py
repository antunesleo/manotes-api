from src import exceptions


class Actor(object):
    pass


class Entity(object):
    pass


class Aggregate(object):
    active_repository = None

    def __init__(self, db_instance):
        self.db_instance = db_instance

    @classmethod
    def create_with_id(cls, id):
        db_instance = cls.active_repository.one_or_none(id=id)
        if db_instance is None:
            raise exceptions.NotFound('Could not find a entity with id {}'.format(id))
        return cls(db_instance=db_instance)

    @classmethod
    def create_with_instance(cls, db_instance):
        return cls(db_instance)

    @classmethod
    def _create_with_keys(cls, **keys):
        db_instance = cls.active_repository.one_or_none(**keys)
        if db_instance is None:
            raise exceptions.NotFound('Could not find a user with keys: {}'.format(keys))
        return cls(db_instance=db_instance)
