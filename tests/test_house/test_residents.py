from tests import base
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


class UserNotesTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.services.NoteService')
    def test_should_call_service_if_not_cached(self, note_service):
        note_service.list_for_user.return_value = []
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        notes = user.notes
        self.assertTrue(note_service.list_for_user.called)
        self.assertEqual(notes, [])

    @base.TestCase.mock.patch('src.house.services.NoteService')
    def test_should_return_notes_if_cached(self, note_service):
        note_service.list_for_user.return_value = []
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user._notes = []
        notes = user.notes
        self.assertFalse(note_service.list_for_user.called)
        self.assertEqual(notes, [])


class UserSharedNotesTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.services.NoteSharingService')
    def test_should_call_note_sharing_service_to_list_for_user_if_not_cached(self, note_sharing_service_mock):
        note_sharing_service_mock.list_it_for_user.return_value = []
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user.shared_notes
        self.assertTrue(note_sharing_service_mock.list_it_for_user.called)
        note_sharing_service_mock.list_it_for_user.assert_called_with(1)

    @base.TestCase.mock.patch('src.house.services.NoteService')
    @base.TestCase.mock.patch('src.house.services.NoteSharingService')
    def test_should_call_note_service_to_create_for_user_if_not_cached(self, note_sharing_service_mock, note_service_mock):
        note_sharing_1 = self.mock.MagicMock(user_id=1, note_id=10)
        note_sharing_2 = self.mock.MagicMock(user_id=1, note_id=20)
        note_sharing_service_mock.list_it_for_user.return_value = [note_sharing_1, note_sharing_2]
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user.shared_notes
        note_service_mock.create_for_user.assert_called_with(1, 20) # TODO: How to test this better?

    @base.TestCase.mock.patch('src.house.services.NoteSharingService')
    def test_should_return_shared_notes_if_cached(self, note_sharing_service_mock):
        note_sharing_service_mock.list_it_for_user.return_value = []
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user._shared_notes = []
        shared_notes = user.shared_notes
        self.assertEqual(shared_notes, [])


class UserTokenTest(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.token = 'ahfhiewuhajhaiu'
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)

    def test_should_return_db_instance_token(self):
        token = self.user.token
        self.assertEqual(token, 'ahfhiewuhajhaiu')


class UserPasswordTest(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.password = 'ahfhiewuhajhaiu'
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)

    def test_should_return_db_instance_password(self):
        password = self.user.password
        self.assertEqual(password, 'ahfhiewuhajhaiu')


class UserUsernameTest(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.username = 'ahfhiewuhajhaiu'
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)

    def test_should_return_db_instance_username(self):
        username = self.user.username
        self.assertEqual(username, 'ahfhiewuhajhaiu')


class UserEmailTest(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.email = 'breno@breno.com'
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)

    def test_should_return_db_instance_email(self):
        email = self.user.email
        self.assertEqual(email, 'breno@breno.com')


class UserAvatarPathTest(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.avatar_path = 'some/path'
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)

    def test_should_return_db_instance_avatar_path(self):
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
        self.user = residents.User(db_instance_mock)

    def test_should_return_dict(self):
        user = self.user.as_dict()
        self.assertIsInstance(user, dict)

    def test_should_return_db_instance_username(self):
        user = self.user.as_dict()
        self.assertTrue(user.get('username'), 'breno')

    def test_should_return_db_instance_email(self):
        user = self.user.as_dict()
        self.assertTrue(user.get('username'), 'breno@breno')


class UserGetANoteTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.services.NoteService')
    def test_should_call_services_to_instantiate(self, note_service_mock):
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user.get_a_note(1)
        self.assertTrue(note_service_mock.create_for_user.called)


class UserCreateANoteTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.services.NoteService')
    def test_should_call_services_to_create_new(self, note_service_mock):
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        note = {
            'id': '1',
            'name': 'this is a note',
            'content': 'This is a note',
            'color': '#FFFFFF'
        }
        user = residents.User(db_instance=db_instance)
        user.create_a_note(note)
        self.assertTrue(note_service_mock.create_new.called)


class UpdateANoteTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.services.NoteService')
    def test_should_call_services_to_instantiate(self, note_service_note):
        note_mock = self.mock.MagicMock()
        note_service_note.create_for_user.return_value = note_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        note_changes = {
            'id': '1',
            'name': 'this is a note',
            'content': 'This is a note',
            'color': '#FFFFFF'
        }
        user.update_a_note(id=1, note_changes=note_changes)
        self.assertTrue(note_service_note.create_for_user.called)

    @base.TestCase.mock.patch('src.house.services.NoteService')
    def test_should_call_update_if_note_was_instantiated(self, note_service_note):
        note_mock = self.mock.MagicMock()
        note_service_note.create_for_user.return_value = note_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        note_changes = {
            'id': '1',
            'name': 'this is a note',
            'content': 'This is a note',
            'color': '#FFFFFF'
        }
        user.update_a_note(id=1, note_changes=note_changes)
        self.assertTrue(note_mock.update.called)


class UserDeleteANoteTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.services.NoteService')
    def test_should_call_services_to_instantiate(self, note_service_note):
        note_mock = self.mock.MagicMock()
        note_service_note.create_for_user.return_value = note_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user.delete_a_note(id=1)
        self.assertTrue(note_service_note.create_for_user)

    @base.TestCase.mock.patch('src.house.services.NoteService')
    def test_should_call_delete_if_note_instantiated(self, note_service_note):
        note_mock = self.mock.MagicMock()
        note_service_note.create_for_user.return_value = note_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user.delete_a_note(id=1)
        self.assertTrue(note_mock.delete.called)


class UserChangeAvatarTest(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)

    @base.mock.patch('src.house.services.FileService.save_avatar', base.mock.MagicMock())
    def test_should_call_avatar_file_to_save(self):
        avatar_mock = self.mock.MagicMock()
        files = {'avatar': avatar_mock}
        self.user.change_avatar(files)
        self.assertTrue(avatar_mock.save.called)

    @base.mock.patch('src.house.services.FileService.save_avatar')
    def test_should_call_file_service_to_save_avatar(self, save_avatar_mock):
        avatar_mock = self.mock.MagicMock()
        files = {'avatar': avatar_mock}
        self.user.change_avatar(files)
        self.assertTrue(save_avatar_mock.called)

    @base.mock.patch('src.house.services.FileService.save_avatar')
    def test_db_instance_has_avatar_path(self, save_avatar_mock):
        avatar_mock = self.mock.MagicMock()
        save_avatar_mock.return_value = 'some/path'
        files = {'avatar': avatar_mock}
        self.user.change_avatar(files)
        self.assertEqual('some/path', self.user.db_instance.avatar_path)

    @base.mock.patch('src.house.services.FileService.save_avatar', base.mock.MagicMock)
    def test_should_call_db_instance_to_save_db(self):
        avatar_mock = self.mock.MagicMock()
        files = {'avatar': avatar_mock}
        self.user.change_avatar(files)
        self.assertTrue(self.user.db_instance.save_db.called)


class UserNoteSharing(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)

    @base.mock.patch('src.house.services.NoteSharingService.share_it_for_me')
    @base.mock.patch('src.house.services.NoteService.create_for_user')
    def test_should_call_note_service_to_create_for_user(self, create_for_user_mock, share_it_for_me_mock):
        self.user.share_a_note(note_id=5, user_id=2)
        create_for_user_mock.assert_called_with(5, 1)
    #
    # @base.mock.patch('src.house.services.UserService.create_with_id')
    # def test_should_call_user_service_to_create_target_user_instance(self, create_with_id_mock):
    #     self.user.share_a_note(note_id=5, target_user_id=2)
    #     create_with_id_mock.assert_called_with(2)

    @base.mock.patch('src.house.services.NoteService.create_for_user')
    @base.mock.patch('src.house.services.UserService.create_with_id')
    @base.mock.patch('src.house.services.NoteSharingService.share_it_for_me')
    def test_should_call_share_service_to_share_a_note(self, share_it_for_me_mock, create_with_id_mock, create_for_user_mock):
        note_mock = self.mock.MagicMock(id=5)
        create_for_user_mock.return_value = note_mock
        self.user.share_a_note(note_id=5, user_id=2)
        share_it_for_me_mock.assert_called_with(1, 5, 2)

    @base.mock.patch('src.house.services.NoteService.create_for_user')
    @base.mock.patch('src.house.services.UserService.create_with_id')
    @base.mock.patch('src.house.services.NoteSharingService.share_it_for_me')
    def test_should_call_note_instance_be_marked_as_shared(self, share_it_for_me_mock, create_with_id_mock, create_for_user_mock):
        note_mock = self.mock.MagicMock()
        create_for_user_mock.return_value = note_mock
        self.user.share_a_note(note_id=5, user_id=2)
        self.assertTrue(note_mock.mark_as_shared.called)
