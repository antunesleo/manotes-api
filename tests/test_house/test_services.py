from tests import base
from src.house import services


@base.TestCase.mock.patch('src.store.reception.Clerk')
class ReceptionServiceCreateClerk(base.TestCase):

    def test_should_create(self, clerk_class_mock):
        clerk_mock = self.mock.MagicMock()
        clerk_class_mock.create.return_value = clerk_mock
        created_clerk = services.ReceptionService.create_clerk()
        self.assertEqual(created_clerk, clerk_mock)


@base.TestCase.mock.patch('src.house.wall.Note')
class WallServicePassTheNoteFactory(base.TestCase):

    def test_should_pass_me_the_factory(self, note_mock):
        note = services.WallService.pass_me_the_note_factory()
        self.assertEqual(note, note_mock)


@base.TestCase.mock.patch('src.house.wall.Note')
class WallServiceCreateNoteForUser(base.TestCase):

    def test_should_create_note_for_user(self, note_factory_mock):
        note_mock = self.mock.MagicMock()
        note_factory_mock.create_for_user.return_value = note_mock
        note = services.WallService.create_note_for_user(1, 1)
        note_factory_mock.create_for_user.assert_called_with(1, 1)
        self.assertEqual(note, note_mock)


@base.TestCase.mock.patch('src.house.residents.User')
class ResidentsServicePassMeTheUserFactory(base.TestCase):

    def test_should_pass_me_the_factory(self, note_mock):
        user_factory = services.ResidentsService.pass_me_the_user_factory()
        self.assertEqual(user_factory, note_mock)


@base.TestCase.mock.patch('src.house.residents.User')
class ResidentsServiceCreateUserWithId(base.TestCase):

    def test_should_create_user(self, user_factory_mock):
        user_mock = self.mock.MagicMock()
        user_factory_mock.create_with_id.return_value = user_mock
        note = services.ResidentsService.create_user_with_id(1)
        user_factory_mock.create_with_id.assert_called_with(1)
        self.assertEqual(note, user_mock)


@base.TestCase.mock.patch('src.house.sharing.NoteSharing')
class SharingServicePassMeTheNoteSharingFactory(base.TestCase):

    def test_should_pass_me_the_factory(self, note_sharing_mock):
        user_factory = services.SharingService.pass_me_the_note_sharing_factory()
        self.assertEqual(user_factory, note_sharing_mock)