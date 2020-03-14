# -*- coding: utf-8 -*-
from src.base.services import Service
from src.central_files import archive


class ClerkService(Service):
    _entity = 'src.store.reception'

    @classmethod
    def create(cls):
        return cls.entity.Clerk.create()


class NoteService(Service):
    _entity = 'src.house.wall'

    @classmethod
    def create_new(cls, note):
        return cls.entity.Note.create_new(note)

    @classmethod
    def list_for_user(cls, user_id):
        return cls.entity.Note.list_for_user(user_id)

    @classmethod
    def create_for_user(cls, id, user_id):
        return cls.entity.Note.create_for_user(id, user_id)

    @classmethod
    def pass_me_the_factory(cls):
        return cls.entity.Note


class FileService(Service):

    @classmethod
    def save_avatar(cls, temp_file_path, user_id):
        file = archive.ScribeFactory.create_with_environment(user_id, router='avatar')
        return file.save(temp_file_path)


class UserService(Service):
    _entity = 'src.house.residents'

    @classmethod
    def pass_me_the_factory(cls):
        return cls.entity.User

    @classmethod
    def create_new(cls, user):
        return cls.entity.User.create_new(user)

    @classmethod
    def create_with_id(cls, user_id):
        return cls.entity.residents.User.create_with_id(user_id)


class NoteSharingService(Service):
    _entity = 'src.house.sharing'

    @classmethod
    def share_it_for_me(cls, giver_id, note_id, target_user_id):
        cls.entity.NoteSharing.share(giver_id, note_id, target_user_id)

    @classmethod
    def list_it_for_user(cls, user_id):
        notes_sharing = cls.entity.NoteSharing.list_for_user(user_id)
        return notes_sharing
