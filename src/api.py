from flask_restful import Api
from src.resource import resources


def create_api(app):
    api = Api(app)
    api.add_resource(resources.NoteResource, '/api/notes', '/api/notes/<int:note_id>')
    api.add_resource(resources.SharedNoteResource, '/api/shared_notes', '/api/shared_notes/<int:note_id>')
    api.add_resource(resources.NoteSharingResource, '/api/me/notes/<int:note_id>/share')
    api.add_resource(resources.AccountResource, '/api/account')
    api.add_resource(resources.LoginResource, '/api/login')
    api.add_resource(resources.AvatarResource, '/api/account/avatar')
    api.add_resource(resources.HealthCheckResource, '/api/healthcheck')
