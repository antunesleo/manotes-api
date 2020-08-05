from tests.unit import base
from src import exceptions
from src.house.application_services import NoteService


class NoteServiceCreate(base.TestCase):

    @base.mock.patch('src.house.services_locator.HouseLocator.pass_me_the_note_class')
    def test_should_create(self, pass_me_the_note_class_mock):
        note_mock = self.mock.MagicMock()
        note_mock.as_dict.return_value = {'name': 'kpkdo jioio', 'content': 'dfjaooeanslkdmks'}
        note_class_mock = self.mock.MagicMock()
        note_class_mock.add.return_value = note_mock
        pass_me_the_note_class_mock.return_value = note_class_mock
        note_service = NoteService()
        create_note_dict = note_service.create(1, {'name': 'kpkdo jioio', 'content': 'dfjaooeanslkdmks'})
        self.assertEqual(create_note_dict, {'name': 'kpkdo jioio', 'content': 'dfjaooeanslkdmks'})
