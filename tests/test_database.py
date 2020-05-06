from tests import base
from src import database


class AppActiveRepositoryTest(base.TestCase):

    def test_has_db(self):
        self.assertTrue(hasattr(database.AppActiveRepository, 'db'))

    def test_has_db_default_none(self):
        # TODO: How to test this? Because the import of initialize on test base made the dependency injection
        pass
