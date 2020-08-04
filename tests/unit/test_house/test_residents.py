from tests.unit import base
from src import config as config_module
from src.house import residents

config = config_module.get_config()


class UserCreateWithToken(base.TestCase):
    @base.TestCase.mock.patch('src.house.residents.User._create_with_keys')
    def test_should_return_instance(self, create_with_keys_mock):
        user_mocked = self.mock.MagicMock('something')
        user_mocked.id = 1
        create_with_keys_mock.return_value = user_mocked
        user_created = residents.User.create_with_token('asfqERafd')
        self.assertEqual(user_created, user_mocked)

    @base.TestCase.mock.patch('src.house.residents.User._create_with_keys')
    def test_should_call_create_with_keys(self, create_with_keys_mock):
        residents.User.create_with_token('asfqERafd')
        create_with_keys_mock.assert_called_with(token='asfqERafd')


class UserCreateWithDictTest(base.TestCase):

    def setUp(self):
        self.user_dict = {
            'id': 1,
            'username': 'breno',
            'email': 'breno@email.com',
            'token': 'ToKeN',
            'password': 'aPkQerT',
            'avatar_path': 'some/path'
        }

    def test_should_create(self):
        user = residents.User.create_with_dict(self.user_dict)
        self.assertIsInstance(user, residents.User)

    def test_should_has_id(self):
        user = residents.User.create_with_dict(self.user_dict)
        self.assertEqual(user.id, 1)

    def test_should_has_username(self):
        user = residents.User.create_with_dict(self.user_dict)
        self.assertEqual(user.username, 'breno')

    def test_should_has_email(self):
        user = residents.User.create_with_dict(self.user_dict)
        self.assertEqual(user.email, 'breno@email.com')

    def test_should_has_password(self):
        user = residents.User.create_with_dict(self.user_dict)
        self.assertEqual(user.password, 'aPkQerT')

    def test_should_has_avatar_path(self):
        user = residents.User.create_with_dict(self.user_dict)
        self.assertEqual(user.avatar_path, 'some/path')


class UserTokenTest(base.TestCase):

    def setUp(self):
        self.db_instance_mock = self.mock.MagicMock()
        self.db_instance_mock.token = 'ahfhiewuhajhaiu'
        self.db_instance_mock.id = 1
        self.user = residents.User(self.db_instance_mock)

    def test_should_return_token_when_not_cached(self):
        token = self.user.token
        self.assertEqual(token, 'ahfhiewuhajhaiu')

    def test_should_return_token_when_cached(self):
        self.user.token
        self.db_instance_mock.token = 'aaaaaa'
        token = self.user.token
        self.assertEqual(token, 'ahfhiewuhajhaiu')


class UserPasswordTest(base.TestCase):

    def setUp(self):
        self.db_instance_mock = self.mock.MagicMock()
        self.db_instance_mock.password = 'ahfhiewuhajhaiu'
        self.db_instance_mock.id = 1
        self.user = residents.User(self.db_instance_mock)

    def test_should_return_password_when_not_cached(self):
        password = self.user.password
        self.assertEqual(password, 'ahfhiewuhajhaiu')

    def test_should_return_password_when_cached(self):
        self.user.password
        self.db_instance_mock.password = 'aaaa'
        password = self.user.password
        self.assertEqual(password, 'ahfhiewuhajhaiu')


class UserUsernameTest(base.TestCase):

    def setUp(self):
        self.db_instance_mock = self.mock.MagicMock()
        self.db_instance_mock.username = 'ahfhiewuhajhaiu'
        self.db_instance_mock.id = 1
        self.user = residents.User(self.db_instance_mock)

    def test_should_return_username_when_not_cached(self):
        username = self.user.username
        self.assertEqual(username, 'ahfhiewuhajhaiu')

    def test_should_return_username_when_cached(self):
        self.user.username
        self.db_instance_mock.username = 'fdfa'
        username = self.user.username
        self.assertEqual(username, 'ahfhiewuhajhaiu')


class UserEmailTest(base.TestCase):

    def setUp(self):
        self.db_instance_mock = self.mock.MagicMock()
        self.db_instance_mock.email = 'breno@breno.com'
        self.db_instance_mock.id = 1
        self.user = residents.User(self.db_instance_mock)

    def test_should_return_email_not_cached(self):
        email = self.user.email
        self.assertEqual(email, 'breno@breno.com')

    def test_should_return_email_cached(self):
        self.user.email
        self.db_instance_mock.email = 'aaaa'
        email = self.user.email
        self.assertEqual(email, 'breno@breno.com')


class UserAvatarPathTest(base.TestCase):

    def setUp(self):
        self.db_instance_mock = self.mock.MagicMock()
        self.db_instance_mock.avatar_path = 'some/path'
        self.db_instance_mock.id = 1
        self.user = residents.User(self.db_instance_mock)

    def test_should_return_db_instance_avatar_ath_when_not_cached(self):
        avatar_path = self.user.avatar_path
        self.assertEqual(avatar_path, 'some/path')

    def test_should_return_db_instance_avatar_path_when_cached(self):
        self.user.avatar_path
        self.db_instance_mock.email = 'aaaa'
        avatar_path = self.user.avatar_path
        self.assertEqual(avatar_path, 'some/path')


class UserCreateWithUsernameTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.residents.User._create_with_keys')
    def test_should_return_instance(self, create_with_keys_mock):
        user_mocked = self.mock.MagicMock('something')
        user_mocked.id = 1
        create_with_keys_mock.return_value = user_mocked
        user_created = residents.User.create_with_username('breno')
        self.assertEqual(user_created, user_mocked)

    @base.TestCase.mock.patch('src.house.residents.User._create_with_keys')
    def test_should_call_create_with_keys(self, create_with_keys_mock):
        residents.User.create_with_username('breno')
        create_with_keys_mock.assert_called_with(username='breno')


class UserCreateWithEmailTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.residents.User._create_with_keys')
    def test_should_return_instance(self, create_with_keys_mock):
        user_mocked = self.mock.MagicMock('something')
        user_mocked.id = 1
        create_with_keys_mock.return_value = user_mocked
        user_created = residents.User.create_with_email('breno@breno.com')
        self.assertEqual(user_created, user_mocked)

    @base.TestCase.mock.patch('src.house.residents.User._create_with_keys')
    def test_should_call_create_with_keys(self, create_with_keys_mock):
        residents.User.create_with_email('breno@breno.com')
        create_with_keys_mock.assert_called_with(email='breno@breno.com')


class UserUpdateTest(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)

    @base.mock.patch('src.house.residents.datetime.datetime')
    def test_should_pop_password_from_payload(self, datetime_mock):
        datetime_mock.utcnow = self.mock.MagicMock()
        payload_mock = self.mock.MagicMock()
        self.user.update(payload_mock)
        self.assertTrue(payload_mock.pop.called)

    @base.mock.patch('src.house.residents.datetime.datetime')
    def test_should_call_datetime_utcnow(self, datetime_mock):
        payload_mock = self.mock.MagicMock()
        self.user.update(payload_mock)
        self.assertTrue(datetime_mock.utcnow.called)

    @base.mock.patch('src.house.residents.datetime.datetime')
    def test_should_set_update_date_from_utcnow(self, datetime_mock):
        datetime_mock.utcnow.return_value = 'asd'
        payload_mock = self.mock.MagicMock()
        self.user.update(payload_mock)
        self.assertTrue(payload_mock.update_date, 'asd')

    @base.mock.patch('src.house.residents.datetime.datetime')
    def test_should_call_db_instance_to_update_from_dict(self, datetime_mock):
        datetime_mock.utcnow = self.mock.MagicMock()
        payload_mock = self.mock.MagicMock()
        self.user.update(payload_mock)
        self.user.db_instance.update_from_dict.assert_called_with(payload_mock)


class UserAsDictTest(base.TestCase):
    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.id = 1
        db_instance_mock.username = 'breno'
        db_instance_mock.email = 'breno@breno'
        db_instance_mock.token = 'ToKeN'
        db_instance_mock.password = '12345'
        db_instance_mock.avatar_path = 'some/path'
        self.user = residents.User(db_instance_mock)

    def test_should_return_dict_when_not_full(self):
        user = self.user.as_dict()
        self.assertIsInstance(user, dict)

    def test_should_return_username_when_not_full(self):
        user = self.user.as_dict()
        self.assertTrue(user.get('username'), 'breno')

    def test_should_return_email_when_not_full(self):
        user = self.user.as_dict()
        self.assertTrue(user.get('username'), 'breno@breno')

    def test_should_return_dict_when_full(self):
        user = self.user.as_dict(full=True)
        self.assertIsInstance(user, dict)

    def test_should_return_db_instance_username_when_full(self):
        user = self.user.as_dict(full=True)
        self.assertTrue(user.get('username'), 'breno')

    def test_should_return_db_instance_email_when_full(self):
        user = self.user.as_dict(full=True)
        self.assertTrue(user.get('username'), 'breno@breno')

    def test_should_return_db_instance_token_when_full(self):
        user = self.user.as_dict(full=True)
        self.assertTrue(user.get('token'), 'ToKeN')

    def test_should_return_db_instance_password_when_full(self):
        user = self.user.as_dict(full=True)
        self.assertTrue(user.get('password'), '12345')

    def test_should_return_db_instance_avatar_path_when_full(self):
        user = self.user.as_dict(full=True)
        self.assertTrue(user.get('avatar_path'), 'some/path')


class UserChangeAvatarTest(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)


