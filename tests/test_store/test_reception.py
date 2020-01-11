from src import exceptions
from src.store import reception
from tests import base


class ClerkCreateAccountTest(base.TestCase):

    def setUp(self):
        pass

    @base.TestCase.mock.patch('src.async_tasks.tasks.start_send_email')
    @base.TestCase.mock.patch('src.security.security_services.TokenService')
    @base.TestCase.mock.patch('src.security.security_services.HashService')
    @base.TestCase.mock.patch('src.house.services.UserService')
    @base.TestCase.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_call_hash_service_to_hash_password(self, is_email_mock, user_service_mock, hash_service_mock, token_service_mock, start_send_email_mock):
        user_mock = self.mock.MagicMock()
        token_service_mock.generate.return_value = 'qwertyasdfgzxcvb'
        hash_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.start_send_email.return_value = 10
        user_service_mock.create_new.return_value = user_mock
        is_email_mock.return_value = True
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        reception.Clerk.create_user_account(payload)
        self.assertTrue(hash_service_mock.hash.called)

    @base.TestCase.mock.patch('src.security.security_services.HashService', base.mock.MagicMock())
    @base.TestCase.mock.patch('src.async_tasks.tasks.start_send_email')
    @base.TestCase.mock.patch('src.security.security_services.TokenService')
    @base.TestCase.mock.patch('src.house.services.UserService')
    @base.TestCase.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_call_token_service_to_generate(self, is_email_mock, user_service_mock, token_service_mock, start_send_email_mock):
        user_mock = self.mock.MagicMock()
        token_service_mock.generate_a_token.return_value = 'qwertyasdfgzxcvb'
        token_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.start_send_email.return_value = 10
        user_service_mock.create_new.return_value = user_mock
        is_email_mock.return_value = True
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        reception.Clerk.create_user_account(payload)
        self.assertTrue(token_service_mock.generate.called)

    @base.TestCase.mock.patch('src.security.security_services.HashService', base.mock.MagicMock())
    @base.TestCase.mock.patch('src.async_tasks.tasks.start_send_email')
    @base.TestCase.mock.patch('src.security.security_services.TokenService')
    @base.TestCase.mock.patch('src.house.services.UserService')
    @base.TestCase.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_call_validation_service_to_validate_email(self, is_email_mock, user_service_mock, token_service_mock, start_send_email_mock):
        user_mock = self.mock.MagicMock()
        token_service_mock.generate_a_token.return_value = 'qwertyasdfgzxcvb'
        token_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.start_send_email.return_value = 10
        user_service_mock.create_new.return_value = user_mock
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        reception.Clerk.create_user_account(payload)
        is_email_mock.assert_called_with('breno@breno.com')

    @base.TestCase.mock.patch('src.security.security_services.HashService', base.mock.MagicMock())
    @base.TestCase.mock.patch('src.async_tasks.tasks.start_send_email')
    @base.TestCase.mock.patch('src.security.security_services.TokenService')
    @base.TestCase.mock.patch('src.house.services.UserService')
    @base.TestCase.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_raise_invalid_email_if_is_email_returns_false(self, is_email_mock, user_service_mock, token_service_mock, start_send_email_mock):
        user_mock = self.mock.MagicMock()
        token_service_mock.generate_a_token.return_value = 'qwertyasdfgzxcvb'
        token_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.start_send_email.return_value = 10
        user_service_mock.create_new.return_value = user_mock
        is_email_mock.return_value = False
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        with self.assertRaises(exceptions.InvalidEmail):
            reception.Clerk.create_user_account(payload)

    @base.TestCase.mock.patch('src.async_tasks.tasks.start_send_email')
    @base.TestCase.mock.patch('src.security.security_services.TokenService')
    @base.TestCase.mock.patch('src.security.security_services.HashService')
    @base.TestCase.mock.patch('src.house.services.UserService')
    @base.TestCase.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_user_service_to_create_new(self, is_email_mock, user_service_mock, hash_service_mock, token_service_mock, start_send_email_mock):
        user_mock = self.mock.MagicMock()
        token_service_mock.generate_a_token.return_value = 'qwertyasdfgzxcvb'
        hash_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.return_value = 10
        user_service_mock.create_new.return_value = user_mock
        is_email_mock.return_value = True
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        reception.Clerk.create_user_account(payload)
        self.assertTrue(user_service_mock.create_new.called)

    @base.TestCase.mock.patch('src.async_tasks.tasks.start_send_email')
    @base.TestCase.mock.patch('src.security.security_services.TokenService')
    @base.TestCase.mock.patch('src.security.security_services.HashService')
    @base.TestCase.mock.patch('src.house.services.UserService')
    @base.TestCase.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_call_tasks_to_start_send_email(self, is_email_mock, user_service_mock, hash_service_mock, token_service_mock, start_send_email_mock):
        user_mock = self.mock.MagicMock()
        token_service_mock.generate.return_value = 'qwertyasdfgzxcvb'
        hash_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.start_send_email.return_value = 10
        user_service_mock.create_from_dict.return_value = user_mock
        is_email_mock.return_value = True
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        reception.Clerk.create_user_account(payload)
        self.assertTrue(start_send_email_mock.called)

    @base.TestCase.mock.patch('src.async_tasks.tasks.start_send_email')
    @base.TestCase.mock.patch('src.security.security_services.TokenService')
    @base.TestCase.mock.patch('src.security.security_services.HashService')
    @base.TestCase.mock.patch('src.house.services.UserService')
    @base.TestCase.mock.patch('src.security.security_services.ValidationService.is_email')
    def test_should_return_user_instance(self, is_email_mock, user_service_mock, hash_service_mock, token_service_mock, start_send_email_mock):
        user_mock = self.mock.MagicMock()
        token_service_mock.generate.return_value = 'qwertyasdfgzxcvb'
        hash_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.start_send_email.return_value = 10
        user_service_mock.create_new.return_value = user_mock
        is_email_mock.return_value = True
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        created_user = reception.Clerk.create_user_account(payload)
        self.assertEqual(created_user, user_mock)
