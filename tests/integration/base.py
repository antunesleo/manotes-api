import unittest, os
from unittest import mock
from unittest.mock import call

from src import initialize, database, models


class TestCase(unittest.TestCase):
    mock = mock

    def setUp(self) -> None:
        database.AppActiveRepository.db.create_all()

    def tearDown(self) -> None:
        for note in models.Note.query.all():
            note.delete_db()
        for user in models.User.query.all():
            user.delete_db()

        database.AppActiveRepository.db.session.remove()
        database.AppActiveRepository.db.drop_all()
