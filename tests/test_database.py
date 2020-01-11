from tests import base
from src import database


class AppRepositoryTest(base.TestCase):

    def test_has_db(self):
        self.assertTrue(hasattr(database.AppRepository, 'db'))

    def test_has_db_default_none(self):
        # TODO: How to test this? Because the import of initialize on test base made the dependency injection
        pass
