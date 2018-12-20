import json
from tests import base
from app import exceptions
from app.resource import resources


class ResourceBaseLoggedUserTest(base.TestCase):

    @base.mock.patch('app.resource.resources.g')
    def test_should_return_user_from_g(self, g_mock):
        user_mock = self.mock.MagicMock()
        g_mock.user = user_mock
        resource_base = resources.ResourceBase()
        self.assertEqual(resource_base.logged_user, user_mock)


class ResourceBaseMeTest(base.TestCase):

    @base.mock.patch('app.resource.resources.ResourceBase.logged_user')
    def test_should_return_me(self, logged_user_mock):
        resource_base = resources.ResourceBase()
        resource_base._me = logged_user_mock
        self.assertEqual(resource_base.me, logged_user_mock)

    @base.mock.patch('app.resource.resources.ResourceBase.logged_user')
    def test_should_set_logged_user_on_me_if_me_is_none(self, logged_user_mock):
        resource_base = resources.ResourceBase()
        resource_base._me = None
        self.assertEqual(resource_base.me, logged_user_mock)


class ResourceBaseClerkTest(base.TestCase):

    @base.mock.patch('app.resource.resources.reception.Clerk')
    def test_should_return_reception_clerk(self, clerk_mock):
        resource_base = resources.ResourceBase()
        self.assertEqual(resource_base.clerk, clerk_mock)


class ResourceBasePayloadTest(base.TestCase):

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_update_payload_with_transformed_if_request_json_is_not_none(self, transform_key_mock, request_mock):
        request_mock.json = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertEqual(payload, {'someKey': 'someValue'})

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_not_update_payload_with_transformed_if_request_json_is_none(self, transform_key_mock, request_mock):
        request_mock.json = None
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertEqual(payload, {})

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_call_transform_key_if_request_json_is_not_none(self, transform_key_mock, request_mock):
        request_mock.json = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue(transform_key_mock.called)

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_not_call_transform_key_if_request_json_is_none(self, transform_key_mock, request_mock):
        request_mock.json = None
        request_mock.form = None
        request_mock.args = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertFalse(transform_key_mock.called)

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_update_payload_with_transformed_if_request_form_is_not_none(self, transform_key_mock, request_mock):
        request_mock.form = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue({'someKey': 'someValue'})

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_not_update_payload_with_transformed_if_request_form_is_none(self, transform_key_mock, request_mock):
        request_mock.form = None
        request_mock.args = None
        request_mock.json = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertEqual(payload, {})

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_call_transform_key_if_request_form_is_not_none(self, transform_key_mock, request_mock):
        request_mock.form = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue(transform_key_mock.called)

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_not_call_transform_key_if_request_form_is_none(self, transform_key_mock, request_mock):
        request_mock.form = None
        request_mock.args = None
        request_mock.json = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertFalse(transform_key_mock.called)

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_update_payload_with_transformed_key_if_request_args_is_not_none(self, transform_key_mock, request_mock):
        request_mock.form = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue({'someKey': 'someValue'})

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_not_update_payload_with_transformed_key_if_request_args_is_none(self, transform_key_mock, request_mock):
        request_mock.form = None
        request_mock.args = None
        request_mock.json = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertEqual(payload, {})

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_call_transform_key_if_request_args_is_not_none(self, transform_key_mock, request_mock):
        request_mock.form = {'some_key': 'some_value'}
        request_mock.args = None
        request_mock.form = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertTrue(transform_key_mock.called)

    @base.mock.patch('app.resource.resources.request')
    @base.mock.patch('app.resource.resources.ResourceBase.transform_key')
    def test_should_not_call_transform_key_if_request_args_is_none(self, transform_key_mock, request_mock):
        request_mock.form = None
        request_mock.args = None
        request_mock.json = None
        transform_key_mock.return_value = {'someKey': 'someValue'}
        resource_base = resources.ResourceBase()
        payload = resource_base.payload
        self.assertFalse(transform_key_mock.called)


class ResourceBaseFilesTest(base.TestCase):

    def test_should_call_request_to_files(self):
        pass

    def test_should_return_files(self):
        pass


class ResourceBaseCamelToSnakeTest(base.TestCase):

    def test_should_call_re_to_sub(self):
        pass

    def test_should_call_re_to_sub_s1(self):
        pass

    def test_should_return_result_lowered(self):
        pass


class ResourceBaseSnakeToCamelTest(base.TestCase):

    def test_should_capitalize_text_after_underscore(self):
        pass

    def test_should_not_capitalize_if_not_underscore(self):
        pass


class ResourceBaseTransformKeyTest(base.TestCase):

    def test_should_for_each_item_on_dict_call_transform_key_with_value_if_data_is_a_dict(self):
        pass

    def test_should_for_each_item_on_dict_call_method_with_key_if_data_is_a_dict(self):
        pass

    def test_should_return_a_dict_if_data_is_a_dict(self):
        pass

    def test_should_for_each_item_on_list_if_data_is_a_list_call_transform_key_with_value_if_item_is_a_dict(self):
        pass

    def test_should_for_each_item_on_list_if_data_is_a_list_call_method_with_key_item_is_a_dict(self):
        pass

    def test_should_return_list_if_data_is_a_list(self):
        pass


class ResourceBaseResponseTest(base.TestCase):

    def test_should_call_transform_key(self):
        pass

    def test_should_return_a_dict(self):
        pass


class ResourceBaseReturnUnexpectedErrorTest(base.TestCase):

    def test_should_return_a_tuple(self):
        pass

    def test_should_return_result_error(self):
        pass

    def test_should_return_internal_server_error(self):
        pass

    def test_should_return_exception_an_unexpected_error_occurred(self):
        pass

    def test_should_return_500(self):
        pass


class ResourceBaseResultOkTest(base.TestCase):

    def test_should_update_result_with_extra_if_extra_is_not_none(self):
        pass

    def test_should_return_dict_result_ok_if_extra_is_none(self):
        pass


class ResourceBaseReturnNotFoundTest(base.TestCase):

    def test_should_return_not_found_if_extra_is_none(self):
        pass

    def test_should_update_result_with_extra_if_extra_is_not_none(self):
        pass

    def test_should_return_404(self):
        pass

    def test_should_return_404_if_extra_is_not_none(self):
        pass


class ResourceBaseReturnNotMineTest(base.TestCase):

    def test_should_return_not_mine_if_extra_is_none(self):
        pass

    def test_should_update_result_with_extra_if_extra_is_not_none(self):
        pass

    def test_should_return_405(self):
        pass

    def test_should_return_405_if_extra_is_not_none(self):
        pass


class AccountResourceGetTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(response.status_code, 405)


class AccountResourceDeleteTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AccountResource()
        response = avatar_resource.delete()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AccountResource()
        response = avatar_resource.delete()
        self.assertEqual(response.status_code, 405)


class AccountResourcePostTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.AccountResource.clerk')
    @base.TestCase.mock.patch('app.resource.resources.AccountResource.payload')
    @base.TestCase.mock.patch('app.resource.resources.g')
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
        account_resource = resources.AccountResource()
        account_resource.post()
        self.assertTrue(clerk_mock.create_user_account.called)

    @base.TestCase.mock.patch('app.resource.resources.AccountResource.clerk')
    @base.TestCase.mock.patch('app.resource.resources.AccountResource.payload')
    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_call_user_to_as_dict(self, g_mock, payload_mock, clerk_mock):
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
        account_resource = resources.AccountResource()
        account_resource.post()
        self.assertTrue(user_mock.as_dict.called)

    @base.TestCase.mock.patch('app.resource.resources.AccountResource.clerk')
    @base.TestCase.mock.patch('app.resource.resources.AccountResource.payload')
    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_user(self, g_mock, payload_mock, clerk_mock):
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
        account_resource = resources.AccountResource()
        response = account_resource.post()
        self.assertEqual(response, {"username": "antunesleo"})


class AccountResourcePutTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_401_if_not_auth(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.AccountResource()
        response = note_resource.put()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_authorized_not_authenticated(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.AccountResource()
        response = note_resource.put()
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('app.resource.resources.AccountResource.me')
    @base.TestCase.mock.patch('app.resource.resources.AccountResource.payload')
    @base.TestCase.mock.patch('app.resource.resources.g')
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
        account_resource = resources.AccountResource()
        account_resource.put()
        self.assertTrue(me_mock.update.called)

    @base.TestCase.mock.patch('app.resource.resources.AccountResource.me')
    @base.TestCase.mock.patch('app.resource.resources.AccountResource.payload')
    @base.TestCase.mock.patch('app.resource.resources.g')
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
        account_resource = resources.AccountResource()
        account_resource.put()
        self.assertTrue(me_mock.as_dict.called)

    @base.TestCase.mock.patch('app.resource.resources.AccountResource.me')
    @base.TestCase.mock.patch('app.resource.resources.AccountResource.payload')
    @base.TestCase.mock.patch('app.resource.resources.g')
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
        account_resource = resources.AccountResource()
        response = account_resource.put()
        self.assertEqual(response, {"username": "antunesleo", "password": "fsfdsafdsa34"})


class LoginResourceGetTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(response.status_code, 405)


class LoginResourcePostTest(base.TestCase):

    def test_should_call_authentication_to_authenticate_with_credentials(self):
        pass

    def test_should_set_user_to_g_if_authenticated(self):
        pass

    def test_should_set_token_to_g_if_authenticated(self):
        pass

    def test_should_return_result_ok_if_authenticate(self):
        pass

    def test_should_return_status_code_200_if_authenticate(self):
        pass

    def test_should_return_not_authorized_if_not_authenticated(self):
        pass

    def test_should_return_status_code_401_if_not_authenticated(self):
        pass

    def test_should_return_not_found_if_user_not_exists_raised(self):
        pass

    def test_should_return_404_if_user_not_exists_raised(self):
        pass


class LoginResourcePutTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.LoginResource()
        response = avatar_resource.put()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.LoginResource()
        response = avatar_resource.put()
        self.assertEqual(response.status_code, 405)


class LoginResourceDeleteTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.delete()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.delete()
        self.assertEqual(response.status_code, 405)


class NoteResourceGetTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_401_if_not_auth(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_authorized_not_authenticated(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_call_me_to_get_a_note(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {'id': 1}
        logged_user_mock.get_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        note_resource.get(1)
        self.assertTrue(note_resource.me.get_a_note.called)

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_return_note(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {'id': 1}
        logged_user_mock.get_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        response = note_resource.get(1)
        self.assertEqual(response, {'id': 1})

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_return_not_mine_if_not_mine_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {'id': 1}
        logged_user_mock.get_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.get(1)
        self.assertEqual(response[0], {'result': 'not-mine', 'error': 'Resource Not Mine', 'id': 1})

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_return_status_code_405_if_not_mine_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {'id': 1}
        logged_user_mock.get_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.get(1)
        self.assertEqual(response[1], 405)

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_authorized_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_401_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.payload')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.payload')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_authorized_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_401_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.payload')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.payload')
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
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = payload_mock
        logged_user_mock.update_a_note.return_value = note_mock
        note_resource = resources.NoteResource()
        response = note_resource.put(1)
        self.assertEqual(response, payload_mock)

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.payload')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.payload')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.payload')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.payload')
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

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_401_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_authorized_if_authentication_fail(self, g_mock):
        g_mock.authenticated = False
        note_resource = resources.NoteResource
        response = note_resource.get()
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {"result": "Not Authorized"})

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_call_me_to_delete_a_note(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock()
        note_resource = resources.NoteResource()
        note_resource.delete(1)
        self.assertTrue(note_resource.me.delete_a_note.called)

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_return_ok(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock()
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertEqual(response, {'result': 'OK'})

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_return_not_found_if_not_found_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock(side_effect=exceptions.NotFound('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertEqual(response[0], {'result': 'not-found', 'error': 'Resource Not Found', 'id': 1})

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_return_status_code_404_if_not_found_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock(side_effect=exceptions.NotFound('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertEqual(response[1], 404)

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_return_not_mine_if_not_mine_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertTrue(note_resource.me.delete_a_note.called)
        self.assertEqual(response[0], {'result': 'not-mine', 'error': 'Resource Not Mine', 'id': 1})

    @base.TestCase.mock.patch('app.resource.resources.g')
    @base.TestCase.mock.patch('app.resource.resources.NoteResource.logged_user')
    def test_should_return_status_code_405_if_not_mine_raised(self, logged_user_mock, g_mock):
        g_mock = self.mock.MagicMock()
        g_mock.authenticated.return_value = True
        logged_user_mock.delete_a_note = self.mock.MagicMock(side_effect=exceptions.NotMine('foo'))
        note_resource = resources.NoteResource()
        response = note_resource.delete(1)
        self.assertTrue(note_resource.me.delete_a_note.called)
        self.assertEqual(response[1], 405)


class AvatarResourceGetTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.get()
        self.assertEqual(response.status_code, 405)


class AvatarResourcePostTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.post()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.post()
        self.assertEqual(response.status_code, 405)


class AvatarResourcePutTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.AvatarResource.files')
    @base.TestCase.mock.patch('app.resource.resources.AvatarResource.me')
    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_call_me_to_change_avatar(self, g_mock, me_mock, files_mock):
        g_mock.authenticated.return_value = True
        me_mock.change_avatar.return_value = None
        avatar_resource = resources.AvatarResource()
        avatar_resource.put()
        me_mock.change_avatar.assert_called_with(files_mock)

    @base.TestCase.mock.patch('app.resource.resources.AvatarResource.files')
    @base.TestCase.mock.patch('app.resource.resources.AvatarResource.me')
    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_ok(self, g_mock, me_mock, files_mock):
        g_mock.authenticated.return_value = True
        me_mock.change_avatar.return_value = None
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.put()
        self.assertEqual(response, {'result': 'OK'})

    @base.TestCase.mock.patch('app.resource.resources.AvatarResource.files')
    @base.TestCase.mock.patch('app.resource.resources.AvatarResource.me')
    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_500_if_exception_raised(self, g_mock, me_mock, files_mock):
        g_mock.authenticated.return_value = True
        me_mock.change_avatar = self.mock.MagicMock(side_effect=Exception)
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.put()
        self.assertEqual(response[1], 500)

    @base.TestCase.mock.patch('app.resource.resources.AvatarResource.files')
    @base.TestCase.mock.patch('app.resource.resources.AvatarResource.me')
    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_unexpected_error_if_exception_raised(self, g_mock, me_mock, files_mock):
        g_mock.authenticated.return_value = True
        me_mock.change_avatar = self.mock.MagicMock(side_effect=Exception)
        avatar_resource = resources.AvatarResource()
        response = avatar_resource.put()
        self.assertEqual(response[0], {'result': 'error', 'error': 'Internal Server Error', 'exception': 'An unexpected error occurred'})


class AvatarResourceDeleteTest(base.TestCase):

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_not_allowed(self, g_mock):
        avatar_resource = resources.AvatarResource
        response = avatar_resource.delete()
        self.assertEqual(json.loads(response.data), {'result': 'Method not allowed'})

    @base.TestCase.mock.patch('app.resource.resources.g')
    def test_should_return_status_code_405(self, g_mock):
        avatar_resource = resources.AvatarResource
        response = avatar_resource.delete()
        self.assertEqual(response.status_code, 405)
