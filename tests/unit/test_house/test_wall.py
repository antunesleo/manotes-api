from tests.unit import base
from src import exceptions
from src.house import wall


class NoteCreateForUserTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.wall.Note.active_repository.one_or_none')
    def test_should_call_repository_to_one_or_none(self, one_or_none_mock):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.user_id = 1
        one_or_none_mock.return_value = db_instance_mock
        wall.Note.create_for_user(1, 1)
        self.assertTrue(one_or_none_mock.called)

    @base.TestCase.mock.patch('src.house.wall.Note.active_repository.one_or_none')
    def test_should_call_return_instance(self, one_or_none_mock):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.user_id = 1
        one_or_none_mock.return_value = db_instance_mock
        created_note = wall.Note.create_for_user(1, 1)
        self.assertTrue(isinstance(created_note, wall.Note))

    @base.TestCase.mock.patch('src.house.wall.Note.active_repository.one_or_none')
    def test_should_return_not_found_if_id_dont_exists(self, one_or_none_mock):
        one_or_none_mock.return_value = None
        with self.assertRaises(exceptions.NotFound):
            wall.Note.create_for_user(1, 1)

    @base.TestCase.mock.patch('src.house.wall.Note.active_repository.one_or_none')
    def test_should_raises_not_mine_if_found_but_user_id_is_different(self, one_or_none_mock):
        db_instance_mock = self.mock.MagicMock()
        db_instance_mock.user_id = 1
        one_or_none_mock.return_value = db_instance_mock
        with self.assertRaises(exceptions.NotMine):
            wall.Note.create_for_user(1, 2)


class NoteCreateNewTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.wall.Note.active_repository.create_from_dict')
    def test_should_call_repository_to_create_from_dict(self, create_from_dict_mock):
        db_instance_mock = self.mock.MagicMock()
        wall.Note.create_new(db_instance_mock)
        self.assertTrue(create_from_dict_mock.called)

    @base.TestCase.mock.patch('src.house.wall.Note.active_repository.create_from_dict')
    def test_should_return_created_instance(self, create_from_dict_mock):
        instance_mock = self.mock.MagicMock()
        create_from_dict_mock.return_value = instance_mock
        created_note = wall.Note.create_new(instance_mock)
        self.assertTrue(isinstance(created_note, wall.Note))


class NoteListForUserTest(base.TestCase):

    @base.TestCase.mock.patch('src.house.wall.Note.active_repository.filter')
    def test_list_for_user_should_call_repository_to_filter(self, filter_mock):
        wall.Note.list_for_user(1)
        self.assertTrue(filter_mock.called)

    @base.TestCase.mock.patch('src.house.wall.Note.active_repository.filter')
    def test_list_for_user_should_return_list(self, filter_mock):
        filter_mock.return_value = []
        notes = wall.Note.list_for_user(1)
        self.assertTrue(isinstance(notes, list))


class NoteUpdateTest(base.TestCase):

    def test_update_should_call_repository_to_update_from_dict(self):
        note = wall.Note.create_with_instance(self.mock.MagicMock())
        note.update({'key': 'value'})
        self.assertTrue(note.db_instance.update_from_dict.called)


class NoteMarkAsShared(base.TestCase):

    def setUp(self):
        self.db_instance = self.mock.MagicMock()
        self.note = wall.Note.create_with_instance(self.db_instance)

    def test_should_set_true_on_shared_db_instance_attribute(self):
        self.note.mark_as_shared()
        self.assertEqual(self.db_instance.shared, True)

    def test_should_call_db_instance_to_save_db(self):
        self.note.mark_as_shared()
        self.assertTrue(self.db_instance.save_db.called)
