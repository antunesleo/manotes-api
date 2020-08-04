class NoteBuilder(object):

    def __init__(self):
        self.note = None

    def build(self):
        return self.note

    def build_a_default(self):
        self.note = {
            'name': 'Note 1',
            'user_id': 1,
            'content': 'This is a note. A note have to have a context. But this one, does not have one!',
            'color': '#eeeeee'
        }
        return self

    def with_user(self, user_id):
        self.note['user_id'] = user_id
        return self
