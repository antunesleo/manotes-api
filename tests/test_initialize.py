from tests import base
from src import config as config_module

config = config_module.get_config()


# class BeforeRequestTest(base.TestCase):
#
#     @base.mock.MagicMock('src.authentication.AuthService.authenticate_with_token')
#     @base.mock.MagicMock('src.initialize.request.cookies')
#     def test_should_call_cookies_to_get_user_token(self, cookies_mock, authenticate_with_token_mock):
#         base.initialize.before_request()
#         self.assertTrue(cookies_mock.called)
#
#     @base.mock.MagicMock('src.authentication.AuthService.authenticate_with_token')
#     @base.mock.MagicMock('src.initialize.request.cookies')
#     def test_should_call_auth_service_to_authenticate_with_token(self, cookies_mock, authenticate_with_token_mock):
#         base.initialize.before_request()
#         self.assertTrue(authenticate_with_token_mock.called)


class AddTokenHeaderTest(base.TestCase):

    @base.mock.patch('src.initialize.g')
    def test_should_call_g_to_get_user(self, g_mock):
        response_mock = self.mock.MagicMock()
        base.initialize.add_token_header(response_mock)
        g_mock.get.assert_called_with("user")

    @base.mock.patch('src.initialize.g')
    def test_g_has_current_token_if_user_is_not_none(self, g_mock):
        response_mock = self.mock.MagicMock()
        g_mock.current_token = 'QQEREQRETYRUTADSGG'
        g_mock.get.return_value = self.mock.MagicMock()
        base.initialize.add_token_header(response_mock)
        self.assertTrue(g_mock.current_token, 'QQEREQRETYRUTADSGG')

    @base.mock.patch('src.initialize.datetime.datetime')
    @base.mock.patch('src.initialize.g')
    def test_should_call_datetime_to_get_time_now(self, g_mock, datetime_mock):
        response_mock = self.mock.MagicMock()
        base.initialize.add_token_header(response_mock)
        self.assertTrue(datetime_mock.now.called)

    @base.mock.patch('src.initialize.datetime')
    @base.mock.patch('src.initialize.g')
    def test_should_call_datetime_to_timedelta_with_90_days(self, g_mock, datetime_mock):
        response_mock = self.mock.MagicMock()
        base.initialize.add_token_header(response_mock)
        datetime_mock.timedelta.assert_called_with(days=90)

    @base.mock.patch('src.initialize.datetime')
    @base.mock.patch('src.initialize.g')
    def test_should_call_response_to_set_user_token_and_expires_date(self, g_mock, datetime_mock):
        g_mock.current_token = 'QQEREQRETYRUTADSGG'
        response_mock = self.mock.MagicMock()
        datetime_mock.datetime.now.return_value = 'A'
        datetime_mock.timedelta.return_value = 'B'
        response = base.initialize.add_token_header(response_mock)
        response.set_cookie.assert_called_with('userToken', 'QQEREQRETYRUTADSGG', expires='AB')


class CreateApiTest(base.TestCase):

    @base.mock.patch('src.api.create_api')
    @base.mock.patch('src.initialize.web_app')
    def test_should_call_api_to_create_api(self, web_app_mock, create_api_mock):
        base.initialize.create_api()
        create_api_mock.assert_called_with(web_app_mock)


class RunTest(base.TestCase):

    @base.mock.patch('src.initialize.web_app')
    @base.mock.patch('src.initialize.create_api')
    def test_should_call_web_app_to_run(self, create_api_mock, web_app_mock):
        base.initialize.run()
        web_app_mock.run.assert_called_with(host='0.0.0.0', port=int(config.PORT), debug=True, threaded=True)
