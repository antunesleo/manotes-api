from flask_restful import Api
from src.resource import resources


def create_api(app):
    api = Api(app)
    api.add_resource(resources.NoteResource, '/api/users/me/notes', '/api/users/me/notes/<int:note_id>')
    api.add_resource(resources.UserResource, '/api/users')
    api.add_resource(resources.LoginResource, '/api/login')
    api.add_resource(resources.AvatarResource, '/api/users/me/avatar')
    api.add_resource(resources.HealthCheckResource, '/api/healthcheck')
