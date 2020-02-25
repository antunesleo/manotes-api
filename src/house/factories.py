from importlib import import_module

from src import exceptions


class ClassProperty(object):
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


def classproperty(func):
    return ClassProperty(func)


class AbstractFactory(object):
    _entity_module = None

    @classproperty
    def entity_module(cls):
        if cls._entity_module is None:
            raise exceptions.InvalidDomain('You should use a specific service implementation')
        try:
            return import_module(cls._entity_module)
        except Exception as ex:
            pass

    @classmethod
    def import_module(cls, _module):
        try:
            return import_module(_module)
        except Exception as ex:
            raise exceptions.InvalidDomain('')

    @classmethod
    def create(cls):
        return cls()


class NoteFactory(AbstractFactory):
    _entity_module = 'src.house.rwall'

    @classmethod
    def create(cls):
        models = cls.import_module('src.models')
        return cls.entity_module.Note(models.Note)
