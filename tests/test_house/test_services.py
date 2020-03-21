from tests import base
from src.house import services


@base.TestCase.mock.patch('src.store.reception.Clerk')
class ReceptionServiceCreateClerk(base.TestCase):

    def test_should_create(self, clerk_class_mock):
        clerk_mock = self.mock.MagicMock()
        clerk_class_mock.create.return_value = clerk_mock
        created_clerk = services.ReceptionService.create_clerk()
        self.assertEqual(created_clerk, clerk_mock)


class WallServiceCreateNewNoteTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.wall.Note')
    def test_create_new_should_call_entity_to_create_new(self, note_mock):
        note_mock.create_new = self.mock.MagicMock(return_value=None)
        services.WallService.create_new_note({'key': 'value'})
        self.assertTrue(note_mock.create_new.called)

    @base.TestCase.mock.patch('src.house.wall.Note')
    def test_create_new_should_return_new_instance_created(self, note_mock):
        new_note_mock = self.mock.MagicMock()
        note_mock.create_new = self.mock.MagicMock(return_value=new_note_mock)
        new_note = services.WallService.create_new_note({'key': 'value'})
        self.assertEqual(new_note_mock, new_note)


class WallServiceListNoteForUserTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.wall.Note')
    def test_list_for_user_should_call_entity_to_list(self, note_mock):
        note_mock.list_for_user = self.mock.MagicMock(return_value=None)
        services.WallService.list_note_for_user(1)
        self.assertTrue(note_mock.list_for_user.called)

    @base.TestCase.mock.patch('src.house.wall.Note')
    def test_list_for_user_should_return_list(self, note_mock):
        note_mock.list_for_user = self.mock.MagicMock(return_value=[])
        notes = services.WallService.list_note_for_user(1)
        self.assertTrue(isinstance(notes, list))


@base.TestCase.mock.patch('src.house.wall.Note')
class WallServicePassTheNoteFactory(base.TestCase):

    def test_should_pass_me_the_factory(self, note_mock):
        note = services.WallService.pass_me_the_note_factory()
        self.assertEqual(note, note_mock)


class FileServiceSaveAvatarTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.services.archive.ScribeFactory')
    def test_should_call_archive_scribe_factory_to_create_with_environment(self, scribe_mock):
        scribe_instance = self.mock.MagicMock()
        scribe_mock.create_with_environment.return_value = scribe_instance
        services.FileService.save_avatar('/some_path', 1)
        scribe_mock.create_with_environment.assert_called_with(1, router='avatar')

    @base.TestCase.mock.patch('src.house.services.archive.ScribeFactory')
    def test_should_call_scribe_to_save(self, scribe_mock):
        scribe_instance = self.mock.MagicMock()
        scribe_mock.create_with_environment.return_value = scribe_instance
        scribe_instance.save.return_value = '/path'
        services.FileService.save_avatar('/some_path', 1)
        scribe_instance.save.assert_called_with('/some_path')

    @base.TestCase.mock.patch('src.house.services.archive.ScribeFactory')
    def test_should_return_file_path(self, scribe_mock):
        scribe_instance = self.mock.MagicMock()
        scribe_mock.create_with_environment.return_value = scribe_instance
        scribe_instance.save.return_value = '/path'
        path = services.FileService.save_avatar('/some_path', 1)
        self.assertEqual('/path', path)


class SharingServiceShareNoteForMe(base.TestCase):

    @base.TestCase.mock.patch('src.house.sharing.NoteSharing.share')
    def test_should_call_note_sharing_to_share(self, share_mock):
        services.SharingService.share_note_for_me(1, 2, 3)
        share_mock.assert_called_with(1, 2, 3)


class SharingServiceListForUser(base.TestCase):

    @base.TestCase.mock.patch('src.house.sharing.NoteSharing.list_for_user')
    def test_should_call_note_sharing_to_list_for_user(self, list_for_user_mock):
        services.SharingService.list_note_sharing_for_user(1)
        list_for_user_mock.assert_called_with(1)

    @base.TestCase.mock.patch('src.house.sharing.NoteSharing.list_for_user')
    def test_should_return_list_of_notes_sharing(self, list_for_user_mock):
        list_for_user_mock.return_value = []
        notes_sharing = services.SharingService.list_note_sharing_for_user(1)
        self.assertEqual(notes_sharing, [])


@base.TestCase.mock.patch('src.house.residents.User')
class ResidentsServicePassMeTheUserFactory(base.TestCase):

    def test_should_pass_me_the_factory(self, note_mock):
        user_factory = services.ResidentsService.pass_me_the_user_factory()
        self.assertEqual(user_factory, note_mock)
