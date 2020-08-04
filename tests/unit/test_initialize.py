from tests.unit import base
from src import config as config_module

config = config_module.get_config()


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
