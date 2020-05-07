class UserBuilder(object):

    def __init__(self):
        self.user = None

    def build(self):
        return self.user

    def build_a_default(self):
        self.user = {
            'username': 'breno',
            'email': 'This is a note. A note have to have a context. But this one, does not have one!',
            'token': 'SoMeToKeN',
            'password': 'someHash',
            'avatar_path': 'some/path',
        }
        return self
