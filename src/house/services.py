# -*- coding: utf-8 -*-
from src.base.services import DIPService


class ReceptionService(DIPService):
    _module = 'src.store.reception'

    @classmethod
    def create_clerk(cls):
        return cls.module.Clerk.create()


class WallService(DIPService):
    _module = 'src.house.wall'

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
    def create_user_with_id(cls, user_id):
        return cls.module.User.create_with_id(user_id)


class SharingService(DIPService):
    _module = 'src.house.sharing'

    @classmethod
    def pass_me_the_note_sharing_factory(cls):
        return cls.module.NoteSharing
