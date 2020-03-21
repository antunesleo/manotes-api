# -*- coding: utf-8 -*-
from src.base.services import DIPService, InfraService
from src.central_files import archive


class ReceptionService(DIPService):
    _module = 'src.store.reception'

    @classmethod
    def create_clerk(cls):
        return cls.module.Clerk.create()


class WallService(DIPService):
    _module = 'src.house.wall'

    @classmethod
    def create_new_note(cls, note):
        return cls.module.Note.create_new(note)

    @classmethod
    def list_note_for_user(cls, user_id):
        return cls.module.Note.list_for_user(user_id)

    @classmethod
    def create_note_for_user(cls, id, user_id):
        return cls.module.Note.create_for_user(id, user_id)

    @classmethod
    def pass_me_the_note_factory(cls):
        return cls.module.Note


class ResidentsService(DIPService):
    _module = 'src.house.residents'

    @classmethod
    def pass_me_the_user_factory(cls):
        return cls.module.User

    @classmethod
    def create_new_user(cls, user):
        return cls.module.User.create_new(user)

    @classmethod
    def create_user_with_id(cls, user_id):
        return cls.module.User.create_with_id(user_id)


class SharingService(DIPService):
    _module = 'src.house.sharing'

    @classmethod
    def share_note_for_me(cls, giver_id, note_id, target_user_id):
        cls.module.NoteSharing.share(giver_id, note_id, target_user_id)

    @classmethod
    def list_note_sharing_for_user(cls, user_id):
        notes_sharing = cls.module.NoteSharing.list_for_user(user_id)
        return notes_sharing


class FileService(InfraService):

    @classmethod
    def save_avatar(cls, temp_file_path, user_id):
        file = archive.ScribeFactory.create_with_environment(user_id, router='avatar')
        return file.save(temp_file_path)
