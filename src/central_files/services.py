from src.base.services import AbsServiceLocator


class ArchiveService(AbsServiceLocator):
    _module = 'src.central_files.archive'

    @classmethod
    def create_scribe_class_for_user(cls, user_id):
        module = cls.module_loader.load(cls._module)
        return module.ScribeFactory.create_with_environment(user_id, router='avatar')
