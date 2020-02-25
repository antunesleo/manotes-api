from tests import base
from src.house.factories import NoteFactory
from src.house.rwall import Note


@base.mock.patch('src.house.factories.AbstractFactory.import_module')
class NoteCreateTest(base.TestCase):

    def test_should_create_note(self, import_module_mock):
        note_mock = self.mock.MagicMock()
        models_mock = self.mock.MagicMock()
        models_mock.Note = note_mock
        import_module_mock.return_value = models_mock
        note = NoteFactory.create()
        self.assertIsInstance(note, Note)

    def test_has_repository(self, import_module_mock):
        note_mock = self.mock.MagicMock()
        models_mock = self.mock.MagicMock()
        models_mock.Note = note_mock
        import_module_mock.return_value = models_mock
        note = NoteFactory.create()
        self.assertEqual(note._repository, note_mock)
