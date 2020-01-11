from tests import base
from src import api


class CreateApiTest(base.TestCase):

    def setUp(self):
        self.app_mock = self.mock.MagicMock()

    @base.mock.patch('src.api.Api')
    def test_should_instantiate_api(self, api_mock):
        api.create_api(self.app_mock)
        self.assertTrue(api_mock.called)

    @base.mock.patch('src.api.Api')
    def test_should_add_NoteResource(self, api_mock):
        api_instance_mock = self.mock.MagicMock()
        api_mock.return_value = api_instance_mock
        api.create_api(self.app_mock)
        self.assertTrue(any(mock_call == base.call(api.resources.NoteResource, '/api/notes', '/api/notes/<int:note_id>')
                            for mock_call in api_instance_mock.add_resource.mock_calls))

    @base.mock.patch('src.api.Api')
    def test_should_add_SharedNoteResource(self, api_mock):
        api_instance_mock = self.mock.MagicMock()
        api_mock.return_value = api_instance_mock
        api.create_api(self.app_mock)
        self.assertTrue(any(mock_call == base.call(api.resources.SharedNoteResource, '/api/shared_notes', '/api/shared_notes/<int:note_id>')
                            for mock_call in api_instance_mock.add_resource.mock_calls))

    @base.mock.patch('src.api.Api')
    def test_should_add_AccountResource(self, api_mock):
        api_instance_mock = self.mock.MagicMock()
        api_mock.return_value = api_instance_mock
        api.create_api(self.app_mock)
        self.assertTrue(any(mock_call == base.call(api.resources.AccountResource, '/api/account')
                            for mock_call in api_instance_mock.add_resource.mock_calls))

    @base.mock.patch('src.api.Api')
    def test_should_add_LoginResource(self, api_mock):
        api_instance_mock = self.mock.MagicMock()
        api_mock.return_value = api_instance_mock
        api.create_api(self.app_mock)
        self.assertTrue(any(mock_call == base.call(api.resources.LoginResource, '/api/login')
                            for mock_call in api_instance_mock.add_resource.mock_calls))

    @base.mock.patch('src.api.Api')
    def test_should_add_AvatarResource(self, api_mock):
        api_instance_mock = self.mock.MagicMock()
        api_mock.return_value = api_instance_mock
        api.create_api(self.app_mock)
        self.assertTrue(any(mock_call == base.call(api.resources.AvatarResource, '/api/account/avatar')
                            for mock_call in api_instance_mock.add_resource.mock_calls))

    @base.mock.patch('src.api.Api')
    def test_should_add_HealthCheckResource(self, api_mock):
        api_instance_mock = self.mock.MagicMock()
        api_mock.return_value = api_instance_mock
        api.create_api(self.app_mock)
        self.assertTrue(any(mock_call == base.call(api.resources.HealthCheckResource, '/api/healthcheck')
                            for mock_call in api_instance_mock.add_resource.mock_calls))
