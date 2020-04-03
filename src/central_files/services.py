from src.base.services import DIPService


class ArchiveService(DIPService):
    _module = 'src.central_files.archive'

    @classmethod
    def create_scribe_factory_for_user(cls, user_id):
        return cls.module.ScribeFactory.create_with_environment(user_id, router='avatar')
