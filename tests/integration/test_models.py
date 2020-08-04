from tests.integration import base

from src import models
from tests.data_builders.builders_wall import NoteBuilder
from tests.data_builders.builders_residents import UserBuilder


class NoteTest(base.TestCase):

    def test_should_filter(self):
        user_dict = UserBuilder().build_a_default().build()
        user = models.User.create_from_dict(user_dict)

        note_dict = NoteBuilder().build_a_default().with_user(user.id).build()
        models.Note.create_from_dict(note_dict)
        models.Note.create_from_dict(note_dict)

        notes = models.Note.filter(user_id=user.id)
        for note in notes:
            self.assertIsInstance(note, models.Note)
            self.assertIsNotNone(note.id)
            self.assertEqual(note_dict['user_id'], note.user_id)
            self.assertEqual(note_dict['name'], note.name)
            self.assertEqual(note_dict['content'], note.content)
            self.assertEqual(note_dict['color'], note.color)
            self.assertIsNotNone(note.creation_date)
            self.assertIsNone(note.update_date)
