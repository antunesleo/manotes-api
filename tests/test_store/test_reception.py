from src import exceptions
from src.store import reception
from tests import base


@base.TestCase.mock.patch('src.async_tasks.tasks.start_send_email')
@base.TestCase.mock.patch('src.security.security_services.TokenService')
@base.TestCase.mock.patch('src.security.security_services.HashService')
@base.TestCase.mock.patch('src.house.services.UserService')
@base.TestCase.mock.patch('src.security.security_services.ValidationService.is_email')
class ClerkCreateAccountTest(base.TestCase):

    def setUp(self):
        self.clerk = reception.Clerk.create()

    def test_should_raise_invalid_email_if_is_email_returns_false(self, is_email_mock, user_service_mock, hash_service_mock, token_service_mock, start_send_email_mock):
        user_mock = self.mock.MagicMock()
        token_service_mock.generate_a_token.return_value = 'qwertyasdfgzxcvb'
        token_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.start_send_email.return_value = 10
        user_service_mock.create_new.return_value = user_mock
        is_email_mock.return_value = False
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        with self.assertRaises(exceptions.InvalidEmail):
            self.clerk.create_user_account(payload)

    def test_should_return_user_dict(self, is_email_mock, user_service_mock, hash_service_mock, token_service_mock, start_send_email_mock):
        token_service_mock.generate.return_value = 'qwertyasdfgzxcvb'
        hash_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.start_send_email.return_value = 10
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {}
        user_factory_mock = self.mock.MagicMock()
        user_factory_mock.create_new.return_value = user_mock
        user_service_mock.pass_me_the_factory.return_value = user_factory_mock
        is_email_mock.return_value = True
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        created_user = self.clerk.create_user_account(payload)
        is_email_mock.assert_called_with('breno@breno.com')
        self.assertTrue(hash_service_mock.hash.called)
        self.assertTrue(token_service_mock.generate.called)
        self.assertEqual(created_user, user_mock.as_dict())

    def test_should_start_send_email_after_user_creation(self, is_email_mock, user_service_mock, hash_service_mock, token_service_mock, start_send_email_mock):
        token_service_mock.generate.return_value = 'qwertyasdfgzxcvb'
        hash_service_mock.hash.return_value = 'qwr324!&8@@333'
        start_send_email_mock.start_send_email.return_value = 10
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {}
        user_factory_mock = self.mock.MagicMock()
        user_factory_mock.create_new.return_value = user_mock
        user_service_mock.pass_me_the_factory.return_value = user_factory_mock
        is_email_mock.return_value = True
        payload = {'username': 'breno', 'email': 'breno@breno.com', 'password': 12345}
        self.clerk.create_user_account(payload)
        is_email_mock.assert_called_with('breno@breno.com')
        self.assertTrue(start_send_email_mock.called)
