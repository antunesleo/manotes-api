from importlib import import_module
from abc import ABC

from src import exceptions


class ModuleLoader(object):

    def load(self, module):
        if module is None:
            raise exceptions.InvalidDomain('You should use a specific service implementation')
        try:
            return import_module(module)
        except Exception as ex:
            pass


class AbsServiceLocator(ABC):
    module_loader = ModuleLoader()


class AbsApplicationService(ABC):
    pass


class AbsDomainService(ABC):
    pass


class AbsInfraService(ABC):
    pass
