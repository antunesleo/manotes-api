# -*- coding: utf-8 -*-
from src.base.services import AbsServiceLocator


class HouseLocator(AbsServiceLocator):

    @classmethod
    def create_clerk(cls):
        module = cls.module_loader.load('src.store.reception')
        return module.Clerk.create()

    @classmethod
    def pass_me_the_note_class(cls):
        module = cls.module_loader.load('src.house.wall')
        return module.Note

    @classmethod
    def pass_me_the_user_class(cls):
        module = cls.module_loader.load('src.house.residents')
        return module.User
