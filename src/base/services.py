from importlib import import_module


class ClassProperty(object):
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


def classproperty(func):
    return ClassProperty(func)


class DIPService(object):
    _module = None

    class InvalidDomain(Exception):
        pass

    @classproperty
    def module(cls):
        if cls._module is None:
            raise cls.InvalidDomain('You should use a specific service implementation')
        try:
            return import_module(cls._module)
        except Exception as ex:
            pass


class DomainService(object):
    pass


class InfraService(object):
    pass
