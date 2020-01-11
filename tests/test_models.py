from tests import base
from src import models, exceptions


class AbstractModelUpdateFromDictTest(base.TestCase):

    @base.TestCase.mock.patch('src.models.AbstractModel.set_values')
    @base.TestCase.mock.patch('src.models.AbstractModel.save_db')
    def test_should_call_save_db(self, save_db_mock, set_values_mock):
        instance = self.mock.MagicMock()
        abstract_model = models.AbstractModel()
        abstract_model.update_from_dict({'oi': 'oi'})
        self.assertTrue(save_db_mock.called)

    @base.TestCase.mock.patch('src.models.AbstractModel.set_values')
    @base.TestCase.mock.patch('src.models.AbstractModel.save_db')
    def test_should_call_set_values(self, save_db_mock, set_values_mock):
        instance = self.mock.MagicMock()
        abstract_model = models.AbstractModel()
        abstract_model.update_from_dict({'oi': 'oi'})
        self.assertTrue(set_values_mock.called)

    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock(side_effect=Exception))
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values', base.mock.MagicMock())
    def test_should_raise_repository_error_if_exception_raised(self):
        abstract_model = models.AbstractModel()
        with self.assertRaises(exceptions.RepositoryError):
            abstract_model.update_from_dict({'key': 'value'})


class AbstractModelSaveDbTest(base.TestCase):

    @base.TestCase.mock.patch('src.models.db')
    def test_should_call_session_to_commit(self, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session

        qm = models.AbstractModel()
        qm.save_db()
        self.assertTrue(session.commit.called)

    @base.TestCase.mock.patch('src.models.db')
    def test_should_call_session_to_add(self, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session

        qm = models.AbstractModel()
        qm.save_db()
        self.assertTrue(session.add.called)

    @base.TestCase.mock.patch('src.models.db')
    def test_should_call_session_to_flush_if_commit_is_false(self, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session

        qm = models.AbstractModel()
        qm.save_db(commit=False)
        self.assertTrue(session.flush.called)


class AbstractModelDeleteDbTest(base.TestCase):

    @base.TestCase.mock.patch('src.models.db')
    def test_should_call_session_to_commit(self, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session

        abstract_model = models.AbstractModel()
        abstract_model.delete_db()
        self.assertTrue(session.commit.called)

    @base.TestCase.mock.patch('src.models.db')
    def test_should_call_session_to_delete(self, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session

        abstract_model = models.AbstractModel()
        abstract_model.delete_db()
        self.assertTrue(session.delete.called)


class AbstractModelCreateFromDict(base.TestCase):

    @base.TestCase.mock.patch('src.models.db')
    @base.TestCase.mock.patch('src.models.AbstractModel.save_db')
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values')
    def test_should_call_set_values(self, set_values_mock, save_db_mock, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session

        abstract_model = models.AbstractModel()
        abstract_model.create_from_dict({'key': 'value'})
        self.assertTrue(set_values_mock.called)

    @base.TestCase.mock.patch('src.models.db')
    @base.TestCase.mock.patch('src.models.AbstractModel.save_db')
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values')
    def test_should_call_save_db(self, set_values_mock, save_db_mock, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session
        abstract_model = models.AbstractModel()
        abstract_model.create_from_dict({'key': 'value'})
        self.assertTrue(set_values_mock.called)

    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock(side_effect=Exception))
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values', base.mock.MagicMock())
    def test_should_raise_repository_error_if_exception_raised(self):
        abstract_model = models.AbstractModel()
        with self.assertRaises(exceptions.RepositoryError):
            abstract_model.create_from_dict({'key': 'value'})


class AbstractModelSetValuesTest(base.TestCase):

    def setUp(self):
        self.abstract_model = models.AbstractModel()
        self.abstract_model.attr1 = ''
        self.abstract_model.attr2 = ''

    # TODO: There is a better way to test this?
    def test_should_set_dict_attr_on_self(self):
        json_data = {'attr1': 1, 'attr2': 2}
        self.abstract_model.set_values(json_data)
        self.assertEqual(self.abstract_model.attr1, 1)
        self.assertEqual(self.abstract_model.attr2, 2)


class UserCreateFromDictTest(base.TestCase):

    def setUp(self):
        self.user = models.User

    @base.TestCase.mock.patch('src.models.db')
    @base.TestCase.mock.patch('src.models.User.save_db')
    @base.TestCase.mock.patch('src.models.User.set_values', base.mock.MagicMock())
    def test_should_call_set_values(self, set_values_mock, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session
        self.user.create_from_dict({'key': 'value'})
        self.assertTrue(set_values_mock.called)

    @base.TestCase.mock.patch('src.models.db')
    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock())
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values')
    def test_should_call_save_db(self, set_values_mock, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session
        self.user.create_from_dict({'key': 'value'})
        self.assertTrue(set_values_mock.called)

    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock(side_effect=Exception))
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values', base.mock.MagicMock())
    def test_should_raise_repository_error_if_exception_raised(self):
        with self.assertRaises(exceptions.RepositoryError):
            self.user.create_from_dict({'key': 'value'})

    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock(side_effect=Exception('manotes_users_email_key')))
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values', base.mock.MagicMock())
    def test_should_raise_EmailAlreadyExists_if_exception_raised_with_manotes_users_email_key_on_message(self):
        with self.assertRaises(exceptions.EmailAlreadyExists):
            self.user.create_from_dict({'key': 'value'})

    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock(side_effect=Exception('manotes_users_username_key')))
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values', base.mock.MagicMock())
    def test_should_raise_EmailAlreadyExists_if_exception_raised_with_manotes_users_username_key_on_message(self):
        with self.assertRaises(exceptions.UsernameAlreadyExists):
            self.user.create_from_dict({'key': 'value'})


class UserUpdateFromDictTest(base.TestCase):

    def setUp(self):
        self.user = models.User()

    @base.TestCase.mock.patch('src.models.db')
    @base.TestCase.mock.patch('src.models.User.save_db')
    @base.TestCase.mock.patch('src.models.User.set_values', base.mock.MagicMock())
    def test_should_call_set_values(self, set_values_mock, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session
        self.user.update_from_dict({'key': 'value'})
        self.assertTrue(set_values_mock.called)

    @base.TestCase.mock.patch('src.models.db')
    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock())
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values')
    def test_should_call_save_db(self, set_values_mock, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session
        self.user.update_from_dict({'key': 'value'})
        self.assertTrue(set_values_mock.called)

    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock(side_effect=Exception))
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values', base.mock.MagicMock())
    def test_should_raise_repository_error_if_exception_raised(self):
        with self.assertRaises(exceptions.RepositoryError):
            self.user.update_from_dict({'key': 'value'})

    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock(side_effect=Exception('manotes_users_email_key')))
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values', base.mock.MagicMock())
    def test_should_raise_EmailAlreadyExists_if_exception_raised_with_manotes_users_email_key_on_message(self):
        with self.assertRaises(exceptions.EmailAlreadyExists):
            self.user.update_from_dict({'key': 'value'})

    @base.TestCase.mock.patch('src.models.AbstractModel.save_db', base.mock.MagicMock(side_effect=Exception('manotes_users_username_key')))
    @base.TestCase.mock.patch('src.models.AbstractModel.set_values', base.mock.MagicMock())
    def test_should_raise_EmailAlreadyExists_if_exception_raised_with_manotes_users_username_key_on_message(self):
        with self.assertRaises(exceptions.UsernameAlreadyExists):
            self.user.create_from_dict({'key': 'value'})
