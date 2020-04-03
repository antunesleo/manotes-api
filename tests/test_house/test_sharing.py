from tests import base
from src import config as config_module, exceptions
from src.house import sharing

config = config_module.get_config()


class NoteSharingShareTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.services.WallService.create_note_for_user')
    @base.TestCase.mock.patch('src.house.services.ResidentsService.create_user_with_id')
    @base.TestCase.mock.patch('src.models.NoteSharing.create_from_dict')
    def test_should_call_repository_to_create_from_dict(self, create_from_dict_mock, create_user_with_id_mock, create_note_for_user_mock):
        sharing.NoteSharing.share(1, 2, 3)
        self.assertTrue(create_from_dict_mock.called)

    @base.TestCase.mock.patch('src.house.services.WallService.create_note_for_user')
    @base.TestCase.mock.patch('src.house.services.ResidentsService.create_user_with_id')
    @base.TestCase.mock.patch('src.models.NoteSharing.create_from_dict')
    def test_should_call_user_service_to_create_with_id(self, create_from_dict_mock, create_user_with_id_mock, create_note_for_user_mock):
        sharing.NoteSharing.share(1, 2, 3)
        create_user_with_id_mock.assert_called_with(3)

    @base.TestCase.mock.patch('src.house.services.WallService.create_note_for_user')
    @base.TestCase.mock.patch('src.house.services.ResidentsService')
    @base.TestCase.mock.patch('src.models.NoteSharing.create_from_dict')
    def test_should_raise_user_not_exists_if_user_service_create_with_id_raises_not_found(self, create_from_dict_mock, residents_service_mock, create_note_for_user_mock):
        residents_service_mock.create_user_with_id = self.mock.MagicMock(side_effect=exceptions.NotFound)
        with self.assertRaises(exceptions.UserNotExists):
            sharing.NoteSharing.share(1, 2, 3)

    @base.TestCase.mock.patch('src.house.services.WallService.create_note_for_user')
    @base.TestCase.mock.patch('src.house.services.ResidentsService.create_user_with_id')
    @base.TestCase.mock.patch('src.models.NoteSharing.create_from_dict')
    def test_should_call_note_service_to_create_for_user(self, create_from_dict_mock, create_user_with_id_mock, create_note_for_user_mock):
        sharing.NoteSharing.share(1, 2, 3)
        create_note_for_user_mock.assert_called_with(2, 1)

    @base.TestCase.mock.patch('src.house.services.WallService')
    @base.TestCase.mock.patch('src.house.services.ResidentsService.create_user_with_id')
    @base.TestCase.mock.patch('src.models.NoteSharing.create_from_dict')
    def test_should_raise_note_note_found_if_note_service_create_for_user_raises_not_found(self, create_from_dict_mock, create_user_with_id_mock, wall_service_mock):
        wall_service_mock.create_note_for_user = self.mock.MagicMock(side_effect=exceptions.NotFound)
        with self.assertRaises(exceptions.NoteNotFound):
            sharing.NoteSharing.share(1, 2, 3)

    @base.TestCase.mock.patch('src.house.services.WallService')
    @base.TestCase.mock.patch('src.house.services.ResidentsService.create_user_with_id')
    @base.TestCase.mock.patch('src.models.NoteSharing.create_from_dict')
    def test_should_raise_note_note_mine_if_note_service_create_for_user_raises_not_mine(self, create_from_dict_mock, create_user_with_id_mock, wall_service_mock):
        wall_service_mock.create_note_for_user = self.mock.MagicMock(side_effect=exceptions.NotMine)
        with self.assertRaises(exceptions.NoteNotMine):
            sharing.NoteSharing.share(1, 2, 3)


class NoteSharingListForUserTest(base.TestCase):

    @base.TestCase.mock.patch('src.models.NoteSharing.filter')
    def test_should_call_repository_to_filter(self, filter_mock):
        sharing.NoteSharing.list_for_user(1)
        filter_mock.assert_called_with(user_id=1)

    @base.TestCase.mock.patch('src.house.sharing.NoteSharing.create_with_instance')
    @base.TestCase.mock.patch('src.models.NoteSharing.filter')
    def test_should_call_create_with_instance_for_each_db_instance(self, filter_mock, create_with_instance_mock):
        note_sharing_1 = self.mock.MagicMock()
        note_sharing_2 = self.mock.MagicMock()
        filter_mock.return_value = [note_sharing_1, note_sharing_2]
        sharing.NoteSharing.list_for_user(1)
        create_with_instance_mock.assert_called_with(note_sharing_2) # How to test it better?
