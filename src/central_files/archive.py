import shutil
import os
import secrets
import boto3
from src import config as config_module
from src import exceptions
from src.security import security_services

config = config_module.get_config()


class ScribeFactory(object):

    @classmethod
    def create_with_environment(cls, user_id, router):
        if config.DEVELOPMENT:
            return LocalScribe.create_with_router_for_user(user_id, router)
        if config.PRODUCTION:
            return S3Scribe.create_with_router_for_user(user_id, router)
        raise exceptions.InvalidEnvironment('Could  not instantiate a file class '
                                 'because the environment config is not development or production')


class AbstractScribe(object):

    def __init__(self, user_id, router):
        self._user_id = user_id
        self._router = router

    @property
    def user_id(self):
        return self._user_id

    @property
    def router(self):
        return self._router

    def save(self, file):
        raise exceptions.NoImplementationError('GOTCHA! You should not instantiate or use methods of an abstract class')


class LocalScribe(AbstractScribe):

    def __init__(self, user_id, router):
        super(LocalScribe, self).__init__(user_id, router)

    @classmethod
    def create_with_router_for_user(cls, user_id, router):
        if router != 'avatar':
            raise exceptions.InvalidRouter('Please pass a valid router for File')

        router = AvatarDirectoryRouter.create_for_user(user_id)
        return cls(user_id, router)

    def save(self, file):
        if not os.path.exists(self.router.path):
            os.makedirs(self.router.path)
        shutil.move(file, self.router.file_path)
        return self.router.file_path


class S3Scribe(AbstractScribe):

    def __init__(self, user_id, router, bucket_name, s3_client):
        super(S3Scribe, self).__init__(user_id, router)
        self.bucket_name = bucket_name
        self.s3_client = s3_client

    @classmethod
    def create_with_router_for_user(cls, user_id, router):
        access_key_id = config.S3_AWS_ACCESS_KEY_ID
        secret_access_key = config.S3_AWS_SECRET_ACCESS_KEY
        bucket_name = config.AVATAR_BUCKET_NAME
        s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
        )

        if router != 'avatar':
            raise exceptions.InvalidRouter('Please pass a valid router for File')

        router = AvatarDirectoryRouter.create_for_user(user_id)
        return cls(user_id, router, bucket_name, s3_client)

    def save(self, file):
        try:
            self.s3_client.upload_file(file, self.bucket_name, self.router.file_name)
        except Exception as ex:
            raise exceptions.UploadFileError('Error uploading file to Amazon S3: {}'.format(str(ex)))
        return self.router.file_name


class AbstractDirectoryRouter(object):

    def __init__(self, user_id):
        self.user_id = user_id


class AvatarDirectoryRouter(AbstractDirectoryRouter):

    def __init__(self, user_id, path, bucket_name, token):
        super(AvatarDirectoryRouter, self).__init__(user_id)
        self.path = path
        self.bucket_name = bucket_name
        self.token = token

    @property
    def file_path(self):
        return '{}avatar-{}-{}.png'.format(self.path, self.token, self.user_id)

    @property
    def file_name(self):
        return 'avatar-{}-{}.png'.format(self.token, self.user_id)

    @classmethod
    def create_for_user(cls, user_id):
        path = '{}/{}/'.format(config.FILE_STORAGE_PATH, config.AVATAR_BUCKET_NAME)
        bucket_name = config.AVATAR_BUCKET_NAME
        token = security_services.TokenService.generate(8)
        return cls(user_id, path, bucket_name, token)
