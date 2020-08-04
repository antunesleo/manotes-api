from tests.unit import base
from src import exceptions
from src.house import wall


class NoteUpdateTest(base.TestCase):

    def test_update_should_call_repository_to_update_from_dict(self):
        note = wall.Note.create_with_instance(self.mock.MagicMock())
        note.update({'key': 'value'})
        self.assertTrue(note.db_instance.update_from_dict.called)
