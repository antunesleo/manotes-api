from tests import base
from src import exceptions
from src.security import authentication


class AuthServiceAuthenticateWithCredentialsTest(base.TestCase):

    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash', base.mock.MagicMock())
    @base.mock.patch('src.house.residents.User.create_with_username', base.mock.MagicMock())
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_call_validation_services_to_check_if_is_email(self, is_email):
        is_email.return_value = False
        authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno', 'password': 12345})
        is_email.assert_called_with('breno')

    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash', base.mock.MagicMock())
    @base.mock.patch('src.house.residents.User.create_with_email')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_call_create_with_email_if_is_email(self, is_email_mock, create_with_email_mock):
        is_email_mock.return_value = True
        authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno', 'password': 12345})
        create_with_email_mock.assert_called_with('breno')

    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash', base.mock.MagicMock())
    @base.mock.patch('src.house.residents.User.create_with_username')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_call_create_with_username_if_is_not_email(self, is_email_mock, create_with_username_mock):
        is_email_mock.return_value = False
        authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno', 'password': 12345})
        create_with_username_mock.assert_called_with('breno')

    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash', base.mock.MagicMock())
    @base.mock.patch('src.house.residents.User.create_with_email', base.mock.MagicMock(side_effect=exceptions.NotFound))
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_raise_user_not_exists_if_not_found_raised_on_create_with_username(self, is_email_mock):
        is_email_mock.return_value = True
        with self.assertRaises(exceptions.UserNotExists):
            authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno', 'password': 12345})

    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash', base.mock.MagicMock())
    @base.mock.patch('src.house.residents.User.create_with_email', base.mock.MagicMock(side_effect=exceptions.NotFound))
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_raise_user_not_exists_if_not_found_raised_one_create_with_email(self, is_email_mock):
        is_email_mock.return_value = True
        with self.assertRaises(exceptions.UserNotExists):
            authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno', 'password': 12345})

    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash')
    @base.mock.patch('src.house.residents.User.create_with_username')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_call_security_service_to_is_strong_equals_to_hash(self, is_email_mock, create_with_username_mock, is_string_equals_to_hash_mock):
        is_email_mock.return_value = False
        user_mock = self.mock.MagicMock()
        user_mock.password = 'fjsadufhnejbadf'
        create_with_username_mock.return_value = user_mock
        authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno', 'password': 12345})
        is_string_equals_to_hash_mock.assert_called_with(12345, 'fjsadufhnejbadf')

    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash')
    @base.mock.patch('src.house.residents.User.create_with_username')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_return_authenticated(self, is_email_mock, create_with_username_mock, is_string_equals_to_hash):
        is_email_mock.return_value = False
        is_string_equals_to_hash.return_value = True
        user_mock = self.mock.MagicMock()
        user_mock.password = 'FHSDAUHENKGA'
        create_with_username_mock.return_value = user_mock
        authenticated, user = authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno', 'password': 12345})
        self.assertTrue(authenticated)

    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash')
    @base.mock.patch('src.house.residents.User.create_with_username')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_return_user_instance(self, is_email_mock, create_with_username_mock, is_string_equals_to_hash):
        is_email_mock.return_value = False
        is_string_equals_to_hash.return_value = True
        user_mock = self.mock.MagicMock()
        user_mock.password = 'FHSDAUHENKGA'
        create_with_username_mock.return_value = user_mock
        authenticated, user = authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno', 'password': 12345})
        self.assertEqual(user, user_mock)


class AuthServiceAuthenticateWithTokenTest(base.TestCase):

    @base.mock.patch('src.security.authentication.g', base.mock.MagicMock())
    @base.mock.patch('src.house.residents.User.create_with_token')
    def test_should_call_create_with_token(self, create_with_token_mock):
        authentication.AuthService.authenticate_with_token('HAUHIAKJA')
        create_with_token_mock.assert_called_with('HAUHIAKJA')

    @base.mock.patch('src.security.authentication.g')
    @base.mock.patch('src.house.residents.User.create_with_token')
    def test_should_set_user_on_g_if_not_found_not_raised(self, create_with_token_mock, g_mock):
        user_mock = self.mock.MagicMock(token='HAIUHIUAAK')
        create_with_token_mock.return_value = user_mock
        authentication.AuthService.authenticate_with_token('HAUHIAKJA')
        self.assertEqual(user_mock, g_mock.user)

    @base.mock.patch('src.security.authentication.g')
    @base.mock.patch('src.house.residents.User.create_with_token')
    def test_should_set_current_token_on_if_not_found_not_raised(self, create_with_token_mock, g_mock):
        user_mock = self.mock.MagicMock(token='HAIUHIUAAK')
        create_with_token_mock.return_value = user_mock
        authentication.AuthService.authenticate_with_token('HAUHIAKJA')
        self.assertEqual(user_mock.token, g_mock.current_token)

    @base.mock.patch('src.security.authentication.g', base.mock.MagicMock())
    @base.mock.patch('src.house.residents.User.create_with_token')
    def test_should_set_authenticated_true_on_g_if_not_found_not_raised(self, create_with_token_mock):
        user_mock = self.mock.MagicMock(token='HAIUHIUAAK')
        create_with_token_mock.return_value = user_mock
        authentication.AuthService.authenticate_with_token('HAUHIAKJA')
        self.assertTrue(user_mock.authenticated)

    @base.mock.patch('src.house.residents.User.create_with_token', base.mock.MagicMock(side_effect=exceptions.NotFound))
    @base.mock.patch('src.security.authentication.g')
    def test_should_set_authenticated_false_on_g_if_not_found_raised(self, g_mock):
        authentication.AuthService.authenticate_with_token('HAUHIAKJA')
        self.assertFalse(g_mock.authenticated)
