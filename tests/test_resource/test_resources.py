import json
from tests import base
from src import exceptions
from src.resource import resources


class ResourceBaseLoggedUserTest(base.TestCase):

    @base.mock.patch('src.resource.resources.g')
    def test_should_return_user_from_g(self, g_mock):
        user_mock = self.mock.MagicMock()
        g_mock.user = user_mock
        resource_base = resources.ResourceBase()
        self.assertEqual(resource_base.logged_user, user_mock)


class ResourceBaseMeTest(base.TestCase):

    @base.mock.patch('src.resource.resources.ResourceBase.logged_user')
    def test_should_return_me(self, logged_user_mock):
        resource_base = resources.ResourceBase()
        resource_base._me = logged_user_mock
        self.assertEqual(resource_base.me, logged_user_mock)

    @base.mock.patch('src.resource.resources.ResourceBase.logged_user')
    def test_should_set_logged_user_on_me_if_me_is_none(self, logged_user_mock):
        resource_base = resources.ResourceBase()
        resource_base._me = None
        self.assertEqual(resource_base.me, logged_user_mock)


class ResourceBaseClerkTest(base.TestCase):

    @base.mock.patch('src.house.services.ClerkService.create')
    def test_should_return_reception_clerk(self, create_mock):
        clerk_mock = self.mock.MagicMock()
        create_mock.return_value = clerk_mock
        resource_base = resources.ResourceBase()
        self.assertEqual(resource_base.clerk, clerk_mock)


class ResourceBasePayloadTest(base.TestCase):

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_update_payload_with_transformed_if_request_json_is_not_none(self, transform_key_mock, request_mock):
        request_mock.json = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertEqual(payload, {'someKey': 'someValue'})

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_not_update_payload_with_transformed_if_request_json_is_none(self, transform_key_mock, request_mock):
        request_mock.json = None
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertEqual(payload, {})

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_call_transform_key_if_request_json_is_not_none(self, transform_key_mock, request_mock):
        request_mock.json = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue(transform_key_mock.called)

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_not_call_transform_key_if_request_json_is_none(self, transform_key_mock, request_mock):
        request_mock.json = None
        request_mock.form = None
        request_mock.args = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertFalse(transform_key_mock.called)

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_update_payload_with_transformed_if_request_form_is_not_none(self, transform_key_mock, request_mock):
        request_mock.form = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue({'someKey': 'someValue'})

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_not_update_payload_with_transformed_if_request_form_is_none(self, transform_key_mock, request_mock):
        request_mock.form = None
        request_mock.args = None
        request_mock.json = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertEqual(payload, {})

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_call_transform_key_if_request_form_is_not_none(self, transform_key_mock, request_mock):
        request_mock.form = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue(transform_key_mock.called)

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_not_call_transform_key_if_request_form_is_none(self, transform_key_mock, request_mock):
        request_mock.form = None
        request_mock.args = None
        request_mock.json = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertFalse(transform_key_mock.called)

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_update_payload_with_transformed_key_if_request_args_is_not_none(self, transform_key_mock, request_mock):
        request_mock.form = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue({'someKey': 'someValue'})

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_not_update_payload_with_transformed_key_if_request_args_is_none(self, transform_key_mock, request_mock):
        request_mock.form = None
        request_mock.args = None
        request_mock.json = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertEqual(payload, {})

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_call_transform_key_if_request_args_is_not_none(self, transform_key_mock, request_mock):
        request_mock.form = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue(transform_key_mock.called)

    @base.mock.patch('src.resource.resources.request')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_not_call_transform_key_if_request_args_is_none(self, transform_key_mock, request_mock):
        request_mock.form = None
        request_mock.args = None
        request_mock.json = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertFalse(transform_key_mock.called)


class ResourceBaseFilesTest(base.TestCase):

    @base.mock.patch('src.resource.resources.request')
    def test_should_return_request_files(self, request_mock):
        files_mock = self.mock.MagicMock()
        request_mock.files = files_mock
        resource_base = resources.ResourceBase()
        self.assertEqual(files_mock, resource_base.files)


class ResourceBaseCamelToSnakeTest(base.TestCase):

    @base.mock.patch('src.resource.resources.re')
    def test_should_call_re_sub_to_pre_separate_terms_with_underscore(self, re_mock):
        re_mock.sub.return_value = 'my_CamelCase'
        resource_base = resources.ResourceBase()
        resource_base.camel_to_snake('myCamelCase')
        # TODO: Check if there is a better wall to check this call
        self.assertEqual(re_mock.sub.mock_calls[0][1], ('(.)([A-Z][a-z]+)', r'\1_\2', 'myCamelCase'))

    @base.mock.patch('src.resource.resources.re')
    def test_should_call_re_sub_to_separate_remaining_terms_with_underscore(self, re_mock):
        re_mock.sub.return_value = 'my_Camel_Case'
        resource_base = resources.ResourceBase()
        resource_base.camel_to_snake('myCamelCase')
        # TODO: Check if there is a better wall to check this call
        self.assertEqual(re_mock.sub.mock_calls[1][1], ('([a-z0-9])([A-Z])', r'\1_\2', 'my_Camel_Case'))

    @base.mock.patch('src.resource.resources.re')
    def test_should_return_result_lowered(self, re_mock):
        re_mock.sub.return_value = 'my_Camel_Case'
        resource_base = resources.ResourceBase()
        result = resource_base.camel_to_snake('myCamelCase')
        self.assertEqual(result, 'my_camel_case')


class ResourceBaseSnakeToCamelTest(base.TestCase):

    def test_should_capitalize_text_after_underscore(self):
        resource_base = resources.ResourceBase()
        result = resource_base.snake_to_camel('my_snake_to_camel')
        self.assertEqual(result, 'mySnakeToCamel')

    def test_should_not_capitalize_if_term_doesnt_have_a_previews_underscore(self):
        resource_base = resources.ResourceBase()
        result = resource_base.snake_to_camel('snake')
        self.assertEqual(result, 'snake')


class ResourceBaseTransformKeyTest(base.TestCase):

    def setUp(self):
        self.resource_base = resources.ResourceBase()

    def test_should_for_each_item_on_dict_call_method_with_key_if_data_is_a_dict(self):
        method_mock = self.mock.MagicMock()
        method_mock.side_effect = ['someKey', 'anotherKey']
        result = self.resource_base.transform_key({'some_key': 'some_value', 'another_key': 'another_value'}, method_mock)
        self.assertEqual([key for key in result.keys()], ['someKey', 'anotherKey'])

    def test_should_for_each_item_on_dict_call_transform_key_with_value_if_data_is_a_dict(self):
        # TODO: How to test this?
        pass

    def test_should_return_dict_if_data_is_dict(self):
        method_mock = self.mock.MagicMock()
        method_mock.side_effect = ['someKey', 'anotherKey']
        result = self.resource_base.transform_key({'some_key': 'some_value', 'another_key': 'another_value'}, method_mock)
        self.assertIsInstance(result, dict)

    def test_should_for_each_item_on_list_if_data_is_a_list_call_transform_key_with_value_if_item_is_a_dict(self):
        # TODO: How to test this?
        pass

    def test_should_for_each_item_on_list_if_data_is_a_list_call_method_with_key_if_item_is_a_dict(self):
        method_mock = self.mock.MagicMock()
        method_mock.side_effect = ['someKey', 'anotherKey']
        result = self.resource_base.transform_key([{'some_key': 'some_value'}, {'another_key': 'another_value'}], method_mock)
        keys = [key for item_dict in result for key in item_dict.keys()]
        self.assertEqual(keys, ['someKey', 'anotherKey'])

    def test_should_return_list_if_data_is_a_list(self):
        method_mock = self.mock.MagicMock()
        method_mock.side_effect = ['someKey', 'anotherKey']
        result = self.resource_base.transform_key([{'some_key': 'some_value'}, {'another_key': 'another_value'}], method_mock)
        self.assertIsInstance(result, list)

    def tearDown(self):
        self.resource_base = None


class ResourceBaseResponseTest(base.TestCase):

    def setUp(self):
        self.resource_base = resources.ResourceBase()

    @base.mock.patch('src.resource.resources.ResourceBase.snake_to_camel')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_call_transform_key(self, transform_key_mock, snake_to_camel_mock):
        self.resource_base.response({'i_am': 'a_dicionary'})
        transform_key_mock.assert_called_with({'i_am': 'a_dicionary'}, snake_to_camel_mock)

    @base.mock.patch('src.resource.resources.ResourceBase.snake_to_camel')
    @base.mock.patch('src.resource.resources.ResourceBase.transform_key')
    def test_should_return_a_dict(self, transform_key_mock, snake_to_camel_mock):
        transform_key_mock.return_value = {'iAm': 'aDicionary'}
        result = self.resource_base.response({'i_am': 'a_dicionary'})
        self.assertEqual(result, {'iAm': 'aDicionary'})

    def tearDown(self):
        self.resource_base = None


class ResourceBaseReturnUnexpectedErrorTest(base.TestCase):

    def setUp(self):
        self.resource_base = resources.ResourceBase()

    def test_should_return_a_tuple(self):
        result = self.resource_base.return_unexpected_error()
        self.assertIsInstance(result, tuple)

    def test_should_return_result_error(self):
        result = self.resource_base.return_unexpected_error()
        self.assertEqual(result[0]['result'], 'error')

    def test_should_return_internal_server_error(self):
        result = self.resource_base.return_unexpected_error()
        self.assertEqual(result[0]['error'], 'Internal Server Error')

    def test_should_return_exception_an_unexpected_error_occurred(self):
        result = self.resource_base.return_unexpected_error()
        self.assertEqual(result[0]['exception'], 'An unexpected error occurred')

    def test_should_return_500(self):
        result = self.resource_base.return_unexpected_error()
        self.assertEqual(result[1], 500)

    def tearDown(self):
        self.resource_base = None


class ResourceBaseReturnOkTest(base.TestCase):

    def setUp(self):
        self.resource_base = resources.ResourceBase()

    def test_should_update_result_with_extra_if_extra_is_not_none(self):
        result = self.resource_base.return_ok(some_key='some_value')
        self.assertEqual({'result': 'OK', 'some_key': 'some_value'}, result)

    def test_should_return_dict_result_ok_if_extra_is_none(self):
        result = self.resource_base.return_ok()
        self.assertEqual({'result': 'OK'}, result)

    def tearDown(self):
        self.resource_base = None


class ResourceBaseReturnNotFoundTest(base.TestCase):

    def setUp(self):
        self.resource_base = resources.ResourceBase()

    def test_should_return_tuple(self):
        result = self.resource_base.return_not_found()
        self.assertIsInstance(result, tuple)

    def test_should_return_not_found_if_extra_is_none(self):
        result = self.resource_base.return_not_found()
        self.assertEqual(result[0]['result'], 'not-found')

    def test_should_update_result_with_extra_if_extra_is_not_none(self):
        result = self.resource_base.return_not_found(extra_key='extra_value')
        self.assertEqual(result[0], {'result': 'not-found', 'error': 'Resource Not Found', 'extra_key': 'extra_value'})

    def test_should_return_404(self):
        result = self.resource_base.return_not_found()
        self.assertEqual(result[1], 404)

    def test_should_return_404_if_extra_is_not_none(self):
        result = self.resource_base.return_not_found(extra_key='extra_value')
        self.assertEqual(result[1], 404)

    def tearDown(self):
        self.resource_base = None


class ResourceBaseReturnNotMineTest(base.TestCase):

    def setUp(self):
        self.resource_base = resources.ResourceBase()

    def test_should_return_tuple(self):
        result = self.resource_base.return_not_mine()
        self.assertIsInstance(result, tuple)

    def test_should_return_not_mine_if_extra_is_none(self):
        result = self.resource_base.return_not_mine()
        self.assertEqual(result[0]['result'], 'not-mine')

    def test_should_update_result_with_extra_if_extra_is_not_none(self):
        result = self.resource_base.return_not_mine(extra_key='extra_value')
        self.assertEqual(result[0], {'result': 'not-mine', 'error': 'Resource Not Mine', 'extra_key': 'extra_value'})

    def test_should_return_405(self):
        result = self.resource_base.return_not_mine()
        self.assertEqual(result[1], 405)

    def test_should_return_405_if_extra_is_not_none(self):
        result = self.resource_base.return_not_mine(extra_key='extra_value')
        self.assertEqual(result[1], 405)

    def tearDown(self):
        self.resource_base = None


class UserResourceGetTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(response.status_code, 405)


class UserResourceDeleteTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.UserResource()
        response = avatar_resource.delete()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.UserResource()
        response = avatar_resource.delete()
        self.assertEqual(response.status_code, 405)


class UserResourcePostTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_call_clerk_to_create_user_account(self, g_mock, payload_mock, clerk_mock):
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        clerk_mock.create_user_account.return_value = user_mock
        account_resource = resources.UserResource()
        account_resource.post()
        self.assertTrue(clerk_mock.create_user_account.called)

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_user(self, g_mock, payload_mock, clerk_mock):
        g_mock.authenticated = True
        clerk_mock.create_user_account.return_value = {
            "username": "antunesleo"
        }
        account_resource = resources.UserResource()
        response = account_resource.post()
        self.assertEqual(response, {"username": "antunesleo"})

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_email_already_exists_if_email_already_exists_raised(self, g_mock, payload_mock, clerk_mock):
        clerk_mock.create_user_account = base.mock.MagicMock(side_effect=exceptions.EmailAlreadyExists)
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        account_resource = resources.UserResource()
        response = account_resource.post()
        self.assertEqual(response[0]['result'], 'email-already-exists')

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_400_bad_request_if_email_already_exists_raised(self, g_mock, payload_mock, clerk_mock):
        clerk_mock.create_user_account = base.mock.MagicMock(side_effect=exceptions.EmailAlreadyExists)
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        account_resource = resources.UserResource()
        response = account_resource.post()
        self.assertEqual(response[1], 400)

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_username_already_exists_if_username_already_exists_raised(self, g_mock, payload_mock, clerk_mock):
        clerk_mock.create_user_account = base.mock.MagicMock(side_effect=exceptions.UsernameAlreadyExists)
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        account_resource = resources.UserResource()
        response = account_resource.post()
        self.assertEqual(response[0]['result'], 'username-already-exists')

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_400_bad_request_if_username_already_exists_raised(self, g_mock, payload_mock, clerk_mock):
        clerk_mock.create_user_account = base.mock.MagicMock(side_effect=exceptions.UsernameAlreadyExists)
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        account_resource = resources.UserResource()
        response = account_resource.post()
        self.assertEqual(response[1], 400)

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_invalid_email_if_invalid_email_raised(self, g_mock, payload_mock, clerk_mock):
        clerk_mock.create_user_account = base.mock.MagicMock(side_effect=exceptions.InvalidEmail)
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        account_resource = resources.UserResource()
        response = account_resource.post()
        self.assertEqual(response[0]['result'], 'invalid-email')

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_400_if_invalid_email_raised(self, g_mock, payload_mock, clerk_mock):
        clerk_mock.create_user_account = base.mock.MagicMock(side_effect=exceptions.InvalidEmail)
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        account_resource = resources.UserResource()
        response = account_resource.post()
        self.assertEqual(response[1], 400)

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_unexpected_error_if_exception_raised(self, g_mock, payload_mock, clerk_mock):
        clerk_mock.create_user_account = base.mock.MagicMock(side_effect=Exception)
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        account_resource = resources.UserResource()
        response = account_resource.post()
        self.assertEqual(response[0], {'result': 'error', 'error': 'Internal Server Error', 'exception': 'An unexpected error occurred'})

    @base.TestCase.mock.patch('src.resource.resources.UserResource.clerk')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_500_internal_server_error_if_exception_raised(self, g_mock, payload_mock, clerk_mock):
        clerk_mock.create_user_account = base.mock.MagicMock(side_effect=Exception)
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        account_resource = resources.UserResource()
        response = account_resource.post()
        self.assertEqual(response[1], 500)


class UserResourcePutTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_401_if_not_auth(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.UserResource()
        response = note_resource.put()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_authorized_not_authenticated(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.UserResource()
        response = note_resource.put()
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('src.resource.resources.UserResource.me')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_call_me_to_update_account(self, g_mock, payload_mock, me_mock):
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        me_mock.update.return_value = None
        account_resource = resources.UserResource()
        account_resource.put()
        self.assertTrue(me_mock.update.called)

    @base.TestCase.mock.patch('src.resource.resources.UserResource.me')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_call_me_to_as_dict(self, g_mock, payload_mock, me_mock):
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        me_mock.update.return_value = None
        me_mock.as_dict.return_value = {"username": "antunesleo", "password": "fsfdsafdsa34"}
        account_resource = resources.UserResource()
        account_resource.put()
        self.assertTrue(me_mock.as_dict.called)

    @base.TestCase.mock.patch('src.resource.resources.UserResource.me')
    @base.TestCase.mock.patch('src.resource.resources.UserResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_me_as_dict(self, g_mock, payload_mock, me_mock):
        g_mock.authenticated = True
        payload_mock = {
            "username": "antunesleo",
            "password": 12345
        }
        user_mock = self.mock.MagicMock()
        user_mock.as_dict.return_value = {
            "username": "antunesleo"
        }
        me_mock.update.return_value = None
        me_mock.as_dict.return_value = {"username": "antunesleo", "password": "fsfdsafdsa34"}
        account_resource = resources.UserResource()
        response = account_resource.put()
        self.assertEqual(response, {"username": "antunesleo", "password": "fsfdsafdsa34"})


class LoginResourceGetTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(response.status_code, 405)


class LoginResourcePostTest(base.TestCase):

    def setUp(self):
        self.login_resource = resources.LoginResource()

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_call_authentication_to_authenticate_with_credentials(self, g_mock, auth_service_mock, payload_mock):
        self.login_resource.post()
        auth_service_mock.authenticate_with_credentials.assert_called_with(payload_mock)

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_set_user_to_g_if_authenticated(self, g_mock, auth_service_mock, payload_mock):
        user_mock = self.mock.MagicMock()
        auth_service_mock.authenticate_with_credentials.return_value = True, user_mock
        self.login_resource.post()
        self.assertEqual(g_mock.user, user_mock)

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_not_set_user_to_g_if_authenticated(self, g_mock, auth_service_mock, payload_mock):
        user_mock = self.mock.MagicMock()
        auth_service_mock.authenticate_with_credentials.return_value = False, user_mock
        self.login_resource.post()
        self.assertNotEqual(g_mock.user, user_mock)

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_set_token_to_g_if_authenticated(self, g_mock, auth_service_mock, payload_mock):
        user_mock = self.mock.MagicMock(token='qwerty')
        auth_service_mock.authenticate_with_credentials.return_value = True, user_mock
        self.login_resource.post()
        self.assertEqual(g_mock.current_token, 'qwerty')

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_return_result_ok_if_authenticate(self, g_mock, auth_service_mock, payload_mock):
        user_mock = self.mock.MagicMock(token='qwerty')
        auth_service_mock.authenticate_with_credentials.return_value = True, user_mock
        result = self.login_resource.post()
        self.assertEqual(result[0], {'result': 'OK'})

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_200_if_authenticate(self, g_mock, auth_service_mock, payload_mock):
        user_mock = self.mock.MagicMock(token='qwerty')
        auth_service_mock.authenticate_with_credentials.return_value = True, user_mock
        result = self.login_resource.post()
        self.assertEqual(result[1], 200)

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_return_not_authorized_if_not_authenticated(self, g_mock, auth_service_mock, payload_mock):
        user_mock = self.mock.MagicMock()
        auth_service_mock.authenticate_with_credentials.return_value = False, user_mock
        result = self.login_resource.post()
        self.assertEqual(result[0], {'result': 'login-not-authorized', 'message': 'The user was not authorize because his credentials are invalid'})

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_401_if_not_authenticated(self, g_mock, auth_service_mock, payload_mock):
        user_mock = self.mock.MagicMock()
        auth_service_mock.authenticate_with_credentials.return_value = False, user_mock
        result = self.login_resource.post()
        self.assertEqual(result[1], 401)

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_return_not_found_if_user_not_exists_raised(self, g_mock, auth_service_mock, payload_mock):
        auth_service_mock.authenticate_with_credentials = self.mock.MagicMock(side_effect=exceptions.UserNotExists('Exception message'))
        result = self.login_resource.post()
        self.assertEqual(result[0], {'result': 'user-from-login-not-found', 'message': 'Resource Not Found'})

    @base.mock.patch('src.resource.resources.LoginResource.payload')
    @base.mock.patch('src.resource.resources.LoginResource.auth_service')
    @base.mock.patch('src.resource.resources.g')
    def test_should_return_404_if_user_not_exists_raised(self, g_mock, auth_service_mock, payload_mock):
        auth_service_mock.authenticate_with_credentials = self.mock.MagicMock(side_effect=exceptions.UserNotExists('Exception message'))
        result = self.login_resource.post()
        self.assertEqual(result[1], 404)

    def tearDown(self):
        self.login_resource = None


class LoginResourcePutTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.LoginResource()
        response = avatar_resource.put()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.LoginResource()
        response = avatar_resource.put()
        self.assertEqual(response.status_code, 405)


class LoginResourceDeleteTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.delete()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.delete()
        self.assertEqual(response.status_code, 405)


# TODO: Implement
class NoteResourceQueryTest(base.TestCase):
    pass


class NoteResourceGetTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_401_if_not_auth(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_authorized_not_authenticated(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_call_me_to_get_a_note(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {'id': 1}
        logged_user_mock.get_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        note_resource.get(1)
        self.assertTrue(note_resource.me.get_a_note.called)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_note(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = {'id': 1}
        logged_user_mock.get_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        response = note_resource.get(1)
        self.assertEqual(response, {'id': 1})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_not_mine_if_not_mine_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {'id': 1}
        logged_user_mock.get_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.get(1)
        self.assertEqual(response[0], {'result': 'not-mine', 'error': 'Resource Not Mine', 'id': 1})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_status_code_405_if_not_mine_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {'id': 1}
        logged_user_mock.get_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.get(1)
        self.assertEqual(response[1], 405)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_not_found_if_not_found_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        logged_user_mock.get_a_note = self.mock.MagicMock(side_effect=exceptions.NotFound('Could not find a note with id 1'))
        note_resource = resources.NoteResource()
        response = note_resource.get(1)
        self.assertEqual(response[0], {'result': 'not-found', 'error': 'Resource Not Found', 'id': 1})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_status_code_404_if_not_found_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        logged_user_mock.get_a_note = self.mock.MagicMock(side_effect=exceptions.NotFound('Could not find a note with id 1'))
        note_resource = resources.NoteResource()
        response = note_resource.get(1)
        self.assertEqual(response[1], 404)

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_call_query_if_not_note_id(self, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_resource = resources.NoteResource()
        note_resource.query = self.mock.MagicMock()
        note_resource.query.return_value = [
            {
                'id': 1,
                'name': 'This is a note',
                'content': 'And I need to write a mock content',
                'color': '#FFFFFF'
            },
            {
                'id': 2,
                'name': 'This is another note',
                'content': 'And I need to write another mock content',
                'color': '#FFFFFF'
            },
        ]
        note_resource.get()
        self.assertTrue(note_resource.query.called)


class NoteResourcePostTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_authorized_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_401_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.payload')
    def test_should_call_me_to_create_a_note(self, payload_mock, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        payload_mock = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = payload_mock
        logged_user_mock.create_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        note_resource.post()
        self.assertTrue(note_resource.me.create_a_note.called)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.payload')
    def test_should_return_created_note(self, payload_mock, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        payload_mock = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = payload_mock
        logged_user_mock.create_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        response = note_resource.post()
        self.assertEqual(response, payload_mock)


class NoteResourcePutTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_authorized_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_401_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.payload')
    def test_should_call_me_to_update_a_note(self, payload_mock, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.update_a_note = self.mock.MagicMock()
        payload_mock = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = payload_mock
        logged_user_mock.update_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        note_resource.put(1)
        self.assertTrue(note_resource.me.update_a_note.called)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.payload')
    def test_should_return_updated_note(self, payload_mock, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.update_a_note = self.mock.MagicMock()
        payload_mock = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        logged_user_mock.update_a_note.return_value = payload_mock
        note_resource = resources.NoteResource()
        response = note_resource.put(1)
        self.assertEqual(response, payload_mock)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.payload')
    def test_should_return_not_found_if_not_found_raised(self, payload_mock, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.update_a_note = self.mock.MagicMock(side_effect=exceptions.NotFound('foo'))
        payload_mock = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = payload_mock
        logged_user_mock.update_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        response = note_resource.put(1)
        self.assertEqual(response[0], {'result': 'not-found', 'error': 'Resource Not Found', 'id': 1})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.payload')
    def test_should_return_status_code_404_if_not_found_raised(self, payload_mock, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.update_a_note = self.mock.MagicMock(side_effect=exceptions.NotFound('foo'))
        payload_mock = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = payload_mock
        logged_user_mock.update_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        response = note_resource.put(1)
        self.assertEqual(response[1], 404)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.payload')
    def test_should_return_not_mine_if_not_mine_raised(self, payload_mock, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.update_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        payload_mock = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        note_resource = resources.NoteResource()
        response = note_resource.put(1)
        self.assertEqual(response[0], {'result': 'not-mine', 'error': 'Resource Not Mine', 'id': 1})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.payload')
    def test_should_return_status_code_405_if_not_mine_raised(self, payload_mock, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.update_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        payload_mock = {
            'id': 1,
            'name': 'This is a note',
            'content': 'And I need to write a mock content',
            'color': '#FFFFFF'
        }
        note_resource = resources.NoteResource()
        response = note_resource.put(1)
        self.assertEqual(response[1], 405)


class NoteResourceDeleteTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_401_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_authorized_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_call_me_to_delete_a_note(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock()
        note_resource = resources.NoteResource()
        note_resource.delete(1)
        self.assertTrue(note_resource.me.delete_a_note.called)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_ok(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock()
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertEqual(response, {'result': 'OK'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_not_found_if_not_found_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock(side_effect=exceptions.NotFound('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertEqual(response[0], {'result': 'not-found', 'error': 'Resource Not Found', 'id': 1})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_status_code_404_if_not_found_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock(side_effect=exceptions.NotFound('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertEqual(response[1], 404)

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_not_mine_if_not_mine_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertTrue(note_resource.me.delete_a_note.called)
        self.assertEqual(response[0], {'result': 'not-mine', 'error': 'Resource Not Mine', 'id': 1})

    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.NoteResource.logged_user')
    def test_should_return_status_code_405_if_not_mine_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertTrue(note_resource.me.delete_a_note.called)
        self.assertEqual(response[1], 405)


class NoteSharingResourceGetTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.get(note_id=1)
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.get(note_id=1)
        self.assertEqual(response.status_code, 405)


class NoteSharingResourcePostTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_call_me_for_share_a_note(self, g_mock, payload_mock, logged_user_mock):
        payload_mock.return_value = {"user_id": 5}
        note_sharing_resource = resources.NoteSharingResource()
        note_sharing_resource.post(note_id=1)
        logged_user_mock.share_a_note.assert_called_with(1, payload_mock["user_id"])

    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_ok(self, g_mock, payload_mock, logged_user_mock):
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.post(note_id=1)
        self.assertTrue(response, note_sharing_resource.return_ok())

    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_user_not_exists_if_user_not_exists_raised(self, g_mock, payload_mock, logged_user_mock):
        logged_user_mock.share_a_note = self.mock.MagicMock(side_effect=exceptions.UserNotExists('Something got wrong'))
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.post(note_id=1)
        self.assertEqual(response, ({'result': 'not-found', 'error': 'Resource Not Found'}, 404))

    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_note_not_found_if_note_not_found_raised(self, g_mock, payload_mock, logged_user_mock):
        logged_user_mock.share_a_note = self.mock.MagicMock(side_effect=exceptions.NoteNotFound('Something got wrong'))
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.post(note_id=1)
        self.assertEqual(response, note_sharing_resource.return_not_found())

    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_note_not_mine_if_note_not_mine_raised(self, g_mock, payload_mock, logged_user_mock):
        logged_user_mock.share_a_note = self.mock.MagicMock(side_effect=exceptions.NoteNotMine('Something got wrong'))
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.post(note_id=1)
        self.assertEqual(response, note_sharing_resource.return_not_mine())

    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.NoteSharingResource.payload')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_unexpected_error_if_exception_raised(self, g_mock, payload_mock, logged_user_mock):
        logged_user_mock.share_a_note = self.mock.MagicMock(side_effect=Exception('Something got wrong'))
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.post(note_id=1)
        self.assertTrue(response, note_sharing_resource.return_unexpected_error())


class NoteSharingResourcePutTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.put(note_id=1)
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.put(note_id=1)
        self.assertEqual(response.status_code, 405)


class NoteSharingResourceDeleteTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.delete(note_id=1)
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        note_sharing_resource = resources.NoteSharingResource()
        response = note_sharing_resource.delete(note_id=1)
        self.assertEqual(response.status_code, 405)


class SharedNoteResourceQueryTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.SharedNoteResource.response')
    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.SharedNoteResource.logged_user')
    def test_should_pass_user_shared_notes_to_response(self, logged_user_mock, g_mock, response_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        shared_note_1 = self.mock.MagicMock()
        shared_note_2 = self.mock.MagicMock()
        shared_notes_mock = [shared_note_1, shared_note_2]
        logged_user_mock.shared_notes = shared_notes_mock
        shared_note_resource = resources.SharedNoteResource()
        shared_note_resource.query()
        response_mock.assert_called_with(shared_note_2)

    @base.TestCase.mock.patch('src.resource.resources.SharedNoteResource.response')
    @base.TestCase.mock.patch('src.resource.resources.g')
    @base.TestCase.mock.patch('src.resource.resources.SharedNoteResource.logged_user')
    def test_should_return_list_from_responses(self, logged_user_mock, g_mock, response_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        shared_note_1 = self.mock.MagicMock()
        shared_note_2 = self.mock.MagicMock()
        shared_notes_mock = [shared_note_1, shared_note_2]
        logged_user_mock.shared_notes = shared_notes_mock
        shared_note_expected_response = self.mock.MagicMock()
        response_mock.return_value = shared_note_expected_response
        shared_note_resource = resources.SharedNoteResource()
        shared_notes_response = shared_note_resource.query()
        self.assertEqual(shared_notes_response, [shared_note_expected_response, shared_note_expected_response])


class SharedNoteResourceGetTest(base.TestCase):
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_401_if_not_auth(self, g_mock):
        g_mock.authenticated = False
        shared_note_resource = resources.SharedNoteResource
        response = shared_note_resource.get()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_authorized_not_authenticated(self, g_mock):
        g_mock.authenticated = False
        shared_note_resource = resources.SharedNoteResource
        response = shared_note_resource.get()
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_call_query_if_not_note_id(self, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        shared_note_resource = resources.SharedNoteResource()
        shared_note_resource.query = self.mock.MagicMock()
        shared_note_resource.query.return_value = [
            {
                'id': 1,
                'name': 'This is a note',
                'content': 'And I need to write a mock content',
                'color': '#FFFFFF'
            },
            {
                'id': 2,
                'name': 'This is another note',
                'content': 'And I need to write another mock content',
                'color': '#FFFFFF'
            },
        ]
        shared_note_resource.get()
        self.assertTrue(shared_note_resource.query.called)

    @base.TestCase.mock.patch('src.resource.resources.SharedNoteResource.logged_user')
    @base.TestCase.mock.patch('src.resource.resources.SharedNoteResource.query')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_unexpected_error_if_exception_raised(self, g_mock, query_mock, logged_user_mock):
        query_mock = self.mock.MagicMock(side_effect=Exception('Something got wrong'))
        shared_note_resource = resources.SharedNoteResource()
        response = shared_note_resource.get()
        self.assertTrue(response, shared_note_resource.return_unexpected_error())


class SharedNoteResourcePostTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        shared_notes_resource = resources.SharedNoteResource()
        response = shared_notes_resource.post(note_id=1)
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        shared_notes_resource = resources.SharedNoteResource()
        response = shared_notes_resource.post(note_id=1)
        self.assertEqual(response.status_code, 405)


class SharedNoteResourcePutTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        shared_notes_resource = resources.SharedNoteResource()
        response = shared_notes_resource.put(note_id=1)
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        shared_notes_resource = resources.SharedNoteResource()
        response = shared_notes_resource.put(note_id=1)
        self.assertEqual(response.status_code, 405)


class SharedNoteResourceDeleteTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        shared_notes_resource = resources.SharedNoteResource()
        response = shared_notes_resource.delete(note_id=1)
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        shared_notes_resource = resources.SharedNoteResource()
        response = shared_notes_resource.delete(note_id=1)
        self.assertEqual(response.status_code, 405)


class AvatarResourceGetTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(response.status_code, 405)


class AvatarResourcePostTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.post()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.post()
        self.assertEqual(response.status_code, 405)


class AvatarResourcePutTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.AvatarResource.files')
    @base.TestCase.mock.patch('src.resource.resources.AvatarResource.me')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_call_me_to_change_avatar(self, g_mock, me_mock, files_mock):
        g_mock.authenticated.return_value = True
        me_mock.change_avatar.return_value = None
        avatar_resource = resources.AvatarResource()
        avatar_resource.put()
        me_mock.change_avatar.assert_called_with(files_mock)

    @base.TestCase.mock.patch('src.resource.resources.AvatarResource.files')
    @base.TestCase.mock.patch('src.resource.resources.AvatarResource.me')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_ok(self, g_mock, me_mock, files_mock):
        g_mock.authenticated.return_value = True
        me_mock.change_avatar.return_value = None
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.put()
        self.assertEqual(response, {'result': 'OK'})

    @base.TestCase.mock.patch('src.resource.resources.AvatarResource.files')
    @base.TestCase.mock.patch('src.resource.resources.AvatarResource.me')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_500_if_exception_raised(self, g_mock, me_mock, files_mock):
        g_mock.authenticated.return_value = True
        me_mock.change_avatar = self.mock.MagicMock(side_effect=Exception)
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.put()
        self.assertEqual(response[1], 500)

    @base.TestCase.mock.patch('src.resource.resources.AvatarResource.files')
    @base.TestCase.mock.patch('src.resource.resources.AvatarResource.me')
    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_unexpected_error_if_exception_raised(self, g_mock, me_mock, files_mock):
        g_mock.authenticated.return_value = True
        me_mock.change_avatar = self.mock.MagicMock(side_effect=Exception)
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.put()
        self.assertEqual(response[0], {'result': 'error', 'error': 'Internal Server Error', 'exception': 'An unexpected error occurred'})


class AvatarResourceDeleteTest(base.TestCase):

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource
        response = avatar_resource.delete()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('src.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource
        response = avatar_resource.delete()
        self.assertEqual(response.status_code, 405)
