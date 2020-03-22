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

    @base.TestCase.mock.patch('src.house.residents.WallService')
    def test_should_call_service_if_not_cached(self, wall_service_mock):
        note_factory_mock = self.mock.MagicMock()
        note_factory_mock.list_note_for_user.return_value = []
        wall_service_mock.pass_me_the_note_factory.return_value = note_factory_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        notes = user.notes
        self.assertTrue(note_factory_mock.list_note_for_user.called)
        self.assertEqual(notes, [])

    @base.TestCase.mock.patch('src.house.residents.WallService')
    def test_should_return_notes_if_cached(self, wall_service):
        wall_service.list_for_user.return_value = []
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user._notes = []
        notes = user.notes
        self.assertFalse(wall_service.list_for_user.called)
        self.assertEqual(notes, [])


class UserSharedNotesTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.residents.SharingService')
    def test_should_call_note_sharing_service_to_list_for_user_if_not_cached(self, sharing_service_mock):
        note_sharing_factory_mock = self.mock.MagicMock()
        note_sharing_factory_mock.list_for_user.return_value = []
        sharing_service_mock.pass_me_the_note_sharing_factory.return_value = note_sharing_factory_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user.shared_notes
        self.assertTrue(note_sharing_factory_mock.list_for_user.called)
        note_sharing_factory_mock.list_for_user.assert_called_with(1)

    @base.TestCase.mock.patch('src.house.residents.WallService')
    @base.TestCase.mock.patch('src.house.residents.SharingService')
    def test_should_call_wall_service_to_create_for_user_if_not_cached(self, sharing_service_mock, wall_service_mock):
        note_sharing_1 = self.mock.MagicMock(user_id=1, note_id=10)
        note_sharing_2 = self.mock.MagicMock(user_id=1, note_id=20)
        note_sharing_factory_mock = self.mock.MagicMock()
        note_sharing_factory_mock.list_for_user.return_value = [note_sharing_1, note_sharing_2]
        sharing_service_mock.pass_me_the_note_sharing_factory.return_value = note_sharing_factory_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user.shared_notes
        wall_service_mock.create_note_for_user.assert_called_with(1, 20) # TODO: How to test this better?

    @base.TestCase.mock.patch('src.house.residents.SharingService')
    def test_should_return_shared_notes_if_cached(self, sharing_service_mock):
        sharing_service_mock.list_note_sharing_for_user.return_value = []
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

    @base.TestCase.mock.patch('src.house.residents.WallService')
    def test_should_call_services_to_instantiate(self, wall_service_mock):
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user.get_a_note(1)
        self.assertTrue(wall_service_mock.create_note_for_user.called)


@base.TestCase.mock.patch('src.house.services.WallService.pass_me_the_note_factory')
class UserCreateANoteTest(base.TestCase):

    def test_should_create_a_note(self, pass_me_the_note_factory_mock):
        note_mock = self.mock.MagicMock()
        pass_me_the_note_factory_mock.return_value = note_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        note_dict = {
            'id': '1',
            'name': 'this is a note',
            'content': 'This is a note',
            'color': '#FFFFFF'
        }
        user = residents.User(db_instance=db_instance)
        user.create_a_note(note_dict)
        self.assertTrue(pass_me_the_note_factory_mock.called)
        note_mock.create_new.assert_called_with(note_dict)

    def test_should_return_created_note(self, pass_me_the_note_factory_mock):
        note_dict_mock = self.mock.MagicMock()
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = note_dict_mock
        note_class_mock = self.mock.MagicMock()
        note_class_mock.create_new.return_value = note_mock
        pass_me_the_note_factory_mock.return_value = note_class_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        note_dict = {
            'id': '1',
            'name': 'this is a note',
            'content': 'This is a note',
            'color': '#FFFFFF'
        }
        user = residents.User(db_instance=db_instance)
        note_dict = user.create_a_note(note_dict)
        self.assertEqual(note_dict_mock, note_dict)


class UpdateANoteTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.residents.WallService')
    def test_should_call_services_to_instantiate(self, wall_service_mock):
        note_mock = self.mock.MagicMock()
        wall_service_mock.create_note_for_user.return_value = note_mock
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
        self.assertTrue(wall_service_mock.create_note_for_user.called)

    @base.TestCase.mock.patch('src.house.residents.WallService')
    def test_should_call_update_if_note_was_instantiated(self, wall_service_mock):
        note_mock = self.mock.MagicMock()
        wall_service_mock.create_note_for_user.return_value = note_mock
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

    @base.TestCase.mock.patch('src.house.residents.WallService')
    def test_should_call_services_to_instantiate(self, wall_service_mock):
        note_mock = self.mock.MagicMock()
        wall_service_mock.create_note_for_user.return_value = note_mock
        db_instance = self.mock.MagicMock()
        db_instance.id = 1
        user = residents.User(db_instance=db_instance)
        user.delete_a_note(id=1)
        self.assertTrue(wall_service_mock.create_note_for_user)

    @base.TestCase.mock.patch('src.house.residents.WallService')
    def test_should_call_delete_if_note_instantiated(self, wall_service_mock):
        note_mock = self.mock.MagicMock()
        wall_service_mock.create_note_for_user.return_value = note_mock
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

    @base.mock.patch('src.house.residents.ArchiveService')
    def test_should_call_scribe_to_save(self, archive_service_mock):
        scribe_mock = self.mock.MagicMock()
        archive_service_mock.create_scribe_factory_for_user.return_value = scribe_mock
        avatar_mock = self.mock.MagicMock()
        files = {'avatar': avatar_mock}
        self.user.change_avatar(files)
        self.assertTrue(scribe_mock.save.called)

    @base.mock.patch('src.house.residents.ArchiveService')
    def test_should_call_avatar_to_save(self, archive_service_mock):
        scribe_mock = self.mock.MagicMock()
        archive_service_mock.create_scribe_factory_for_user.return_value = scribe_mock
        avatar_mock = self.mock.MagicMock()
        files = {'avatar': avatar_mock}
        self.user.change_avatar(files)
        self.assertTrue(avatar_mock.save.called)

    @base.mock.patch('src.house.residents.ArchiveService')
    def test_db_instance_has_avatar_path(self, archive_service_mock):
        scribe_mock = self.mock.MagicMock()
        scribe_mock.save.return_value = 'some/path'
        archive_service_mock.create_scribe_factory_for_user.return_value = scribe_mock
        files = {'avatar': self.mock.MagicMock()}
        self.user.change_avatar(files)
        self.assertEqual('some/path', self.user.db_instance.avatar_path)

    @base.mock.patch('src.house.residents.ArchiveService')
    def test_should_call_db_instance_to_save_db(self, archive_service_mock):
        avatar_mock = self.mock.MagicMock()
        files = {'avatar': avatar_mock}
        self.user.change_avatar(files)
        self.assertTrue(self.user.db_instance.save_db.called)


class UserNoteSharing(base.TestCase):

    def setUp(self):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.id = 1
        self.user = residents.User(db_instance_mock)

    @base.mock.patch('src.house.services.SharingService.pass_me_the_note_sharing_factory')
    @base.mock.patch('src.house.services.WallService.create_note_for_user')
    def test_should_call_wall_service_to_create_for_user(self, create_note_for_user_mock, pass_me_the_note_sharing_factory_mock):
        self.user.share_a_note(note_id=5, user_id=2)
        create_note_for_user_mock.assert_called_with(5, 1)

    @base.mock.patch('src.house.services.WallService.create_note_for_user')
    @base.mock.patch('src.house.services.ResidentsService.create_user_with_id')
    @base.mock.patch('src.house.services.SharingService.pass_me_the_note_sharing_factory')
    def test_should_call_share_service_to_share_a_note(self, pass_me_the_note_sharing_factory_mock, create_user_with_id_mock, create_note_for_user_mock):
        sharing_factory_mock = self.mock.MagicMock()
        pass_me_the_note_sharing_factory_mock.return_value = sharing_factory_mock

        note_mock = self.mock.MagicMock(id=5)
        create_note_for_user_mock.return_value = note_mock
        self.user.share_a_note(note_id=5, user_id=2)
        sharing_factory_mock.share.assert_called_with(1, 5, 2)

    @base.mock.patch('src.house.services.WallService.create_note_for_user')
    @base.mock.patch('src.house.services.ResidentsService.create_user_with_id')
    @base.mock.patch('src.house.services.SharingService.pass_me_the_note_sharing_factory')
    def test_should_call_note_instance_to_be_marked_as_shared(self, pass_me_the_note_sharing_factory_mock, create_user_with_id_mock, create_note_for_user_mock):
        sharing_factory_mock = self.mock.MagicMock()
        pass_me_the_note_sharing_factory_mock.return_value = sharing_factory_mock
        note_mock = self.mock.MagicMock()
        create_note_for_user_mock.return_value = note_mock
        self.user.share_a_note(note_id=5, user_id=2)
        self.assertTrue(note_mock.mark_as_shared.called)
