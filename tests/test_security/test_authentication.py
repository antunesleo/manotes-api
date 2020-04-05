from tests import base
from src import exceptions
from src.security import authentication


class AuthServiceAuthenticateWithCredentialsTest(base.TestCase):

    @base.mock.patch('src.security.security_services.EncodingService.encode')
    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash')
    @base.mock.patch('src.house.residents.User.create_with_email')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_authenticate_when_credentials_has_email_and_credentials_is_valid(self, is_email_mock, create_with_email_mock, is_string_equals_to_hash_mock, encode_mock):
        is_email_mock.return_value = True
        user_mock = self.mock.MagicMock()
        create_with_email_mock.return_value = user_mock
        encode_mock.return_value = 'EnCoDeDuSeR'
        is_string_equals_to_hash_mock.return_value = True
        is_auth, user = authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno@email.com', 'password': 12345})
        self.assertTrue(is_auth)
        self.assertEqual(user, user_mock)
        self.assertEqual(user_mock.encoded_token, 'EnCoDeDuSeR')

    @base.mock.patch('src.security.security_services.EncodingService.encode')
    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash')
    @base.mock.patch('src.house.residents.User.create_with_username')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_authenticate_when_has_username_and_credentials_is_valid(self, is_email_mock, create_with_username_mock, is_string_equals_to_hash_mock, encode_mock):
        is_email_mock.return_value = False
        user_mock = self.mock.MagicMock()
        create_with_username_mock.return_value = user_mock
        encode_mock.return_value = 'EnCoDeDuSeR'
        is_string_equals_to_hash_mock.return_value = True
        is_auth, user = authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno@email.com', 'password': 12345})
        self.assertTrue(is_auth)
        self.assertEqual(user, user_mock)
        self.assertEqual(user_mock.encoded_token, 'EnCoDeDuSeR')

    @base.mock.patch('src.security.security_services.EncodingService.encode')
    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash')
    @base.mock.patch('src.house.residents.User.create_with_email')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_not_authenticate_when_has_email_and_credentials_is_invalid(self, is_email_mock, create_with_email_mock, is_string_equals_to_hash_mock, encode_mock):
        is_email_mock.return_value = True
        user_mock = self.mock.MagicMock()
        create_with_email_mock.return_value = user_mock
        encode_mock.return_value = 'EnCoDeDuSeR'
        is_string_equals_to_hash_mock.return_value = False
        is_auth, user = authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno@email.com', 'password': 12345})
        self.assertFalse(is_auth)
        self.assertEqual(user, user_mock)

    @base.mock.patch('src.security.security_services.EncodingService.encode')
    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash')
    @base.mock.patch('src.house.residents.User.create_with_username')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_not_authenticate_when_has_username_and_credentials_is_invalid(self, is_email_mock, create_with_username_mock, is_string_equals_to_hash_mock, encode_mock):
        is_email_mock.return_value = False
        user_mock = self.mock.MagicMock()
        create_with_username_mock.return_value = user_mock
        encode_mock.return_value = 'EnCoDeDuSeR'
        is_string_equals_to_hash_mock.return_value = False
        is_auth, user = authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno', 'password': 12345})
        self.assertFalse(is_auth)
        self.assertEqual(user, user_mock)

    @base.mock.patch('src.security.security_services.EncodingService.encode', base.mock.MagicMock())
    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash', base.mock.MagicMock())
    @base.mock.patch('src.house.residents.User.create_with_email')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_raise_user_not_exists_when_has_email_and_users_not_found(self, is_email_mock, create_with_email_mock):
        is_email_mock.return_value = True
        create_with_email_mock.side_effect = exceptions.NotFound
        with self.assertRaises(exceptions.UserNotExists):
            authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno@email.com', 'password': 12345})

    @base.mock.patch('src.security.security_services.EncodingService.encode', base.mock.MagicMock())
    @base.mock.patch('src.security.security_services.HashService.is_string_equals_to_hash', base.mock.MagicMock())
    @base.mock.patch('src.house.residents.User.create_with_username')
    @base.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_raise_user_not_exists_when_has_username_and_users_not_found(self, is_email_mock, create_with_username_mock):
        is_email_mock.return_value = False
        create_with_username_mock.side_effect = exceptions.NotFound
        with self.assertRaises(exceptions.UserNotExists):
            authentication.AuthService.authenticate_with_credentials({'username_or_email': 'breno@email.com', 'password': 12345})


class AuthServiceCheckAuthorizationTest(base.TestCase):

   def test_should_authorizate(self):
       pass

   def test_should_not_authorizate_if_user_not_found(self):
       pass

   def test_should_not_authorizate_if_decoding_error(self):
       pass
