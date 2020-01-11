from src import exceptions
from tests import base
from src.base import domain


class EntityCreateWithIdTest(base.TestCase):
    @base.TestCase.mock.patch('src.base.domain.Entity.repository')
    def test_should_call_repository_one_or_none(self, repository_mock):
        domain.Entity.create_with_id(1)
        self.assertTrue(repository_mock.one_or_none)

    @base.TestCase.mock.patch('src.base.domain.Entity.repository')
    def test_should_return_instance(self, repository_mock):
        db_instance_mock = self.mock.MagicMock()
        repository_mock.one_or_none.return_value = db_instance_mock
        created_note = domain.Entity.create_with_id(1)
        self.assertTrue(isinstance(created_note, domain.Entity))

    @base.TestCase.mock.patch('src.base.domain.Entity.repository')
    def test_should_raise_not_found_if_id_dont_exists(self, repository_mock):
        repository_mock.one_or_none.return_value = None
        with self.assertRaises(exceptions.NotFound):
            domain.Entity.create_with_id(1)


class EntityCreateWithInstanceTest(base.TestCase):
    def test_create_with_instance_should_return_instance(self):
        instance_mocked = self.mock.MagicMock('something')
        instance_mocked.id = 1
        entity_created = domain.Entity.create_with_instance(instance_mocked)
        self.assertTrue(isinstance(entity_created, domain.Entity))


class EntityCreateWithKeysTest(base.TestCase):
    @base.TestCase.mock.patch('src.base.domain.Entity.repository')
    def test_should_return_instance(self, repository_mock):
        user_mocked = self.mock.MagicMock('something')
        user_mocked.id = 1
        repository_mock.one_or_none.return_value = user_mocked
        entity_created = domain.Entity._create_with_keys(breno='breno')
        self.assertTrue(isinstance(entity_created, domain.Entity))

    @base.TestCase.mock.patch('src.base.domain.Entity.repository')
    def test_should_pass_keys_to_repository(self, repository_mock):
        user_mocked = self.mock.MagicMock('something')
        user_mocked.id = 1
        repository_mock.one_or_none.return_value = user_mocked
        domain.Entity._create_with_keys(breno='breno')
        repository_mock.one_or_none.assert_called_with(breno='breno')

    @base.TestCase.mock.patch('src.base.domain.Entity.repository')
    def test_should_raise_not_found_if_one_or_none_returns_none(self, repository_mock):
        repository_mock.one_or_none.return_value = None
        with self.assertRaises(exceptions.NotFound):
            domain.Entity._create_with_keys(breno='breno')
