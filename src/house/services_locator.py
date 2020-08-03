# -*- coding: utf-8 -*-
from src.base.services import AbsServiceLocator


class HouseLocator(AbsServiceLocator):

    @classmethod
    def create_clerk(cls):
        module = cls.module_loader.load('src.store.reception')
        return module.Clerk.create()

    @classmethod
    def create_note_for_user(cls, id, user_id):
        module = cls.module_loader.load('src.house.wall')
        return module.Note.create_for_user(id, user_id)

    @classmethod
    def pass_me_the_note_class(cls):
        module = cls.module_loader.load('src.house.wall')
        return module.Note

    @classmethod
    def pass_me_the_user_class(cls):
        module = cls.module_loader.load('src.house.residents')
        return module.User

    @classmethod
    def create_user_with_id(cls, user_id):
        module = cls.module_loader.load('src.house.residents')
        return module.User.create_with_id(user_id)

    @classmethod
    def pass_me_the_note_sharing_class(cls):
        module = cls.module_loader.load('src.house.sharing')
        return module.NoteSharing
