# -*- coding: utf-8 -*-
from src.base.services import Service
from src.central_files import archive
from src.house import residents, sharing


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
    def update_by_id(cls, id, changed_note, user_id):
        note = cls.entity.Note.create_for_user(id, user_id)
        note.update(changed_note)
        return note


class FileService(Service):

    @classmethod
    def save_avatar(cls, temp_file_path, user_id):
        file = archive.ScribeFactory.create_with_environment(user_id, router='avatar')
        return file.save(temp_file_path)


class UserService(Service):

    @classmethod
    def create_new(cls, user):
        return residents.User.create_new(user)

    @classmethod
    def create_with_id(cls, user_id):
        return residents.User.create_with_id(user_id)


class NoteSharingService(Service):

    @classmethod
    def share_it_for_me(cls, giver_id, note_id, target_user_id):
        sharing.NoteSharing.share(giver_id, note_id, target_user_id)

    @classmethod
    def list_it_for_user(cls, user_id):
        notes_sharing = sharing.NoteSharing.list_for_user(user_id)
        return notes_sharing
