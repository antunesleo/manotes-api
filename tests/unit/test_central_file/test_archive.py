from tests.unit import base
from src import exceptions
from src.central_files import archive


class ScribeFactoryCreateWithEnvironmentTest(base.TestCase):

    @base.mock.patch('src.central_files.archive.LocalScribe')
    @base.mock.patch('src.central_files.archive.config')
    def test_should_call_local_scribe_to_create_with_router_for_user_if_config_is_development(self, config_mock, local_scribe_mock):
        config_mock.PRODUCTION = None
        config_mock.DEVELOPMENT.return_value = self.mock.MagicMock()
        archive.ScribeFactory.create_with_environment(1, self.mock.MagicMock())
        self.assertTrue(local_scribe_mock.create_with_router_for_user.called)

    @base.mock.patch('src.central_files.archive.S3Scribe')
    @base.mock.patch('src.central_files.archive.config')
    def test_should_call_s3_scribe_to_create_with_router_for_user_if_config_is_production(self, config_mock, s3_scribe_mock):
        # INFO: Feature disabled because I don't have an AWS account
        # config_mock.DEVELOPMENT = None
        # config_mock.PRODUCTION.return_value = self.mock.MagicMock()
        # archive.ScribeFactory.create_with_environment(1, self.mock.MagicMock())
        # self.assertTrue(s3_scribe_mock.create_with_router_for_user.called)
        pass

    @base.mock.patch('src.central_files.archive.config')
    def test_should_raise_invalid_env_if_config_nether_development_or_production(self, config_mock):
        config_mock.DEVELOPMENT = None
        config_mock.PRODUCTION = None
        with self.assertRaises(exceptions.InvalidEnvironment):
            archive.ScribeFactory.create_with_environment(1, self.mock.MagicMock())


class AbstractScribeInitTest(base.TestCase):

    def setUp(self):
        self.abstract_scribe = archive.AbstractScribe(1, self.mock.MagicMock())

    def test_has_user_id(self):
        self.assertTrue(hasattr(self.abstract_scribe, 'user_id'))

    def test_has_router(self):
        self.assertTrue(hasattr(self.abstract_scribe, 'router'))


class AbstractScribeSaveTest(base.TestCase):

    def test_should_raise_not_implemented(self):
        abstract_scribe = archive.AbstractScribe(1, self.mock.MagicMock())
        with self.assertRaises(exceptions.NoImplementationError):
            abstract_scribe.save(file=self.mock.MagicMock())


class AbstractScribeUserIdTest(base.TestCase):

    def test_has_user_id(self):
        abstract_scribe = archive.AbstractScribe(1, self.mock.MagicMock())
        self.assertEqual(1, abstract_scribe.user_id)


class AbstractScribeRouterTest(base.TestCase):

    def test_has_router(self):
        router_mock = self.mock.MagicMock()
        abstract_scribe = archive.AbstractScribe(1, router_mock)
        self.assertEqual(router_mock, abstract_scribe.router)


class LocalScribeCreateWithRouterForUserTest(base.TestCase):

    def test_should_raise_invalid_router_if_router_is_not_avatar(self):
        with self.assertRaises(exceptions.InvalidRouter):
            archive.LocalScribe.create_with_router_for_user(1, 'asdf')

    @base.mock.patch('src.central_files.archive.AvatarDirectoryRouter.create_for_user')
    def test_should_call_avatar_directory_router_to_create_for_user_if_router_is_avatar(self, create_for_user_mock):
        archive.LocalScribe.create_with_router_for_user(1, 'avatar')
        self.assertTrue(create_for_user_mock.called)

    def test_should_return_instance(self):
        local_scribe_instance = archive.LocalScribe.create_with_router_for_user(1, 'avatar')
        self.assertIsInstance(local_scribe_instance, archive.LocalScribe)


class LocalScribeSaveTest(base.TestCase):

    def setUp(self):
        self.local_scribe = archive.LocalScribe(1, self.mock.MagicMock(file_path='/some/path'))

    @base.mock.patch('src.central_files.archive.shutil')
    @base.mock.patch('src.central_files.archive.os')
    def test_should_call_os_to_check_if_path_exists(self, os_mock, shutil_mock):
        self.local_scribe.save(self.mock.MagicMock())
        self.assertTrue(os_mock.path.exists.called)

    @base.mock.patch('src.central_files.archive.shutil')
    @base.mock.patch('src.central_files.archive.os')
    def test_should_call_os_to_makedirs_if_path_dont_exists(self, os_mock, shutil_mock):
        path_mock = self.mock.MagicMock
        exists_mock = self.mock.MagicMock()
        exists_mock.return_value = False
        path_mock.exists = exists_mock
        os_mock.path = path_mock
        self.local_scribe.save(self.mock.MagicMock())
        self.assertTrue(os_mock.makedirs.called)

    @base.mock.patch('src.central_files.archive.shutil')
    @base.mock.patch('src.central_files.archive.os')
    def test_should_call_shutil_to_move_file_to_router_path(self, os_mock, shutil_mock):
        self.local_scribe.save(self.mock.MagicMock())
        self.assertTrue(shutil_mock.move.called)

    @base.mock.patch('src.central_files.archive.shutil')
    @base.mock.patch('src.central_files.archive.os')
    def test_should_return_router_file_path(self, os_mock, shutil_mock):
        result = self.local_scribe.save(self.mock.MagicMock())
        self.assertTrue(result, '/some/path')


class S3ScribeInit(base.TestCase):

    def setUp(self):
        self.s3_scribe = archive.S3Scribe(1, self.mock.MagicMock(), 'bucket_name', 's3_client')

    def test_has_user_id(self):
        self.assertTrue(hasattr(self.s3_scribe, 'user_id'))

    def test_has_bucket_name(self):
        self.assertTrue(hasattr(self.s3_scribe, 'bucket_name'))

    def test_has_s3_client(self):
        self.assertTrue(hasattr(self.s3_scribe, 's3_client'))


class S3ScribeCreateWithRouterForUserTest(base.TestCase):

    @base.mock.patch('src.central_files.archive.config.S3_AWS_ACCESS_KEY_ID', 'AFDSFASDDFAS')
    @base.mock.patch('src.central_files.archive.config.S3_AWS_SECRET_ACCESS_KEY', 'QERQEWE')
    @base.mock.patch('src.central_files.archive.config.AVATAR_BUCKET_NAME', 'ZXCV')
    @base.mock.patch('src.central_files.archive.AvatarDirectoryRouter.create_for_user', base.mock.MagicMock())
    @base.mock.patch('src.central_files.archive.boto3')
    def test_should_get_call_boto3_to_instantiate_client(self, boto_3_mock):
        archive.S3Scribe.create_with_router_for_user(1, 'avatar')
        boto_3_mock.client.assert_called_with(
            's3',
            aws_access_key_id='AFDSFASDDFAS',
            aws_secret_access_key='QERQEWE',
        )

    @base.mock.patch('src.central_files.archive.config.S3_AWS_ACCESS_KEY_ID', 'AFDSFASDDFAS')
    @base.mock.patch('src.central_files.archive.config.S3_AWS_SECRET_ACCESS_KEY', 'QERQEWE')
    @base.mock.patch('src.central_files.archive.config.AVATAR_BUCKET_NAME', 'ZXCV')
    @base.mock.patch('src.central_files.archive.boto3.client', base.mock.MagicMock())
    def test_should_raise_invalid_router_if_router_is_not_avatar(self):
        with self.assertRaises(exceptions.InvalidRouter):
            archive.S3Scribe.create_with_router_for_user(1, 'qwerty')

    @base.mock.patch('src.central_files.archive.config.S3_AWS_ACCESS_KEY_ID', 'AFDSFASDDFAS')
    @base.mock.patch('src.central_files.archive.config.S3_AWS_SECRET_ACCESS_KEY', 'QERQEWE')
    @base.mock.patch('src.central_files.archive.config.AVATAR_BUCKET_NAME', 'ZXCV')
    @base.mock.patch('src.central_files.archive.boto3.client', base.mock.MagicMock())
    @base.mock.patch('src.central_files.archive.AvatarDirectoryRouter.create_for_user')
    def test_should_call_avatar_directory_router_to_create_for_user(self, create_for_user_mock):
        archive.S3Scribe.create_with_router_for_user(1, 'avatar')
        create_for_user_mock.assert_called_with(1)

    @base.mock.patch('src.central_files.archive.config.S3_AWS_ACCESS_KEY_ID', 'AFDSFASDDFAS')
    @base.mock.patch('src.central_files.archive.config.S3_AWS_SECRET_ACCESS_KEY', 'QERQEWE')
    @base.mock.patch('src.central_files.archive.config.AVATAR_BUCKET_NAME', 'ZXCV')
    @base.mock.patch('src.central_files.archive.boto3.client', base.mock.MagicMock())
    @base.mock.patch('src.central_files.archive.AvatarDirectoryRouter.create_for_user', base.mock.MagicMock())
    def test_should_return_instance(self):
        instance = archive.S3Scribe.create_with_router_for_user(1, 'avatar')
        self.assertIsInstance(instance, archive.S3Scribe)


class S3ScribeSaveTest(base.TestCase):

    def setUp(self):
        self.file_name = 'asd'
        router_mock = self.mock.MagicMock(file_name=self.file_name)
        # TODO: Is this mock right?
        self.s3_scribe = archive.S3Scribe(1, router_mock, 'bucket_name', self.mock.MagicMock())

    def test_should_call_s3_client_to_upload_file(self):
        self.s3_scribe.save('image.png')
        self.assertTrue(self.s3_scribe.s3_client.upload_file.called)

    def test_should_raise_upload_file_error_if_upload_file_raises_exception(self):
        self.s3_scribe.s3_client.upload_file = self.mock.MagicMock(side_effect=Exception)
        with self.assertRaises(exceptions.UploadFileError):
            self.s3_scribe.save('image.png')

    def test_should_return_router_file_name(self):
        file_name = self.s3_scribe.save('image.png')
        self.assertEqual(file_name, self.file_name)


class AbstractDirectoryRouterInitTest(base.TestCase):

    def setUp(self):
        self.abstract_directory_router = archive.AbstractDirectoryRouter(1)

    def test_has_user_id(self):
        self.assertTrue(hasattr(self.abstract_directory_router, 'user_id'))


class AvatarDirectoryRouterInitTest(base.TestCase):

    def setUp(self):
        self.avatar_directory_router = archive.AvatarDirectoryRouter(1, 'path', 'bucket_name', 'token')

    def test_has_path(self):
        self.assertTrue(hasattr(self.avatar_directory_router, 'path'))

    def test_has_bucket_name(self):
        self.assertTrue(hasattr(self.avatar_directory_router, 'bucket_name'))

    def test_has_token(self):
        self.assertTrue(hasattr(self.avatar_directory_router, 'token'))


class AvatarDirectoryRouterFilePathTest(base.TestCase):

    def setUp(self):
        self.user_id = 1
        self.path = 'path/'
        self.bucket_name = 'bucket_name'
        self.token = 'token'
        self.avatar_directory_router = archive.AvatarDirectoryRouter(self.user_id, self.path, self.bucket_name, self.token)

    def test_should_use_path_to_construct_file_path(self):
        used_path = '{}/'.format(self.avatar_directory_router.file_path.split('/')[0])
        self.assertTrue(self.path == used_path)

    def test_should_use_token_to_construct_file_path(self):
        self.assertTrue(self.token == self.avatar_directory_router.file_path.split('-')[1])

    def test_should_use_user_id_to_construct_file_path(self):
        self.assertTrue(str(self.user_id) == self.avatar_directory_router.file_path.split('-')[2].split('.')[0])

    def test_should_return_file_path_with_png_extension(self):
        self.assertTrue('png' == self.avatar_directory_router.file_path.split('.')[1])


class AvatarDirectoryRouterFileNameTest(base.TestCase):

    def setUp(self):
        self.user_id = 1
        self.path = 'path/'
        self.bucket_name = 'bucket_name'
        self.token = 'token'
        self.avatar_directory_router = archive.AvatarDirectoryRouter(self.user_id, self.path, self.bucket_name, self.token)

    def test_should_use_token_to_construct_file_name(self):
        self.assertTrue(self.token == self.avatar_directory_router.file_name.split('-')[1])

    def test_should_use_user_id_to_construct_file_name(self):
        self.assertTrue(str(self.user_id) == self.avatar_directory_router.file_name.split('-')[2].split('.')[0])


class AvatarDirectoryRouterCreateForUser(base.TestCase):

    @base.mock.patch('src.central_files.archive.config.FILE_STORAGE_PATH', 'some/path')
    @base.mock.patch('src.central_files.archive.config.AVATAR_BUCKET_NAME', 'somename')
    @base.mock.patch('src.security.security_services.TokenService.generate')
    def test_should_make_path_with_FILE_STORAGE_PATH_and_AVATAR_BUCKET_NAME(self, generate_mock):
        generate_mock.return_value = 'FSSDAGETEQE'
        avatar_directory_router = archive.AvatarDirectoryRouter.create_for_user(1)
        self.assertTrue(avatar_directory_router.path, 'some/path')

    @base.mock.patch('src.central_files.archive.config.FILE_STORAGE_PATH', 'some/path')
    @base.mock.patch('src.central_files.archive.config.AVATAR_BUCKET_NAME', 'somename')
    @base.mock.patch('src.security.security_services.TokenService.generate')
    def test_should_call_token_service_to_generate(self, generate_mock):
        generate_mock.return_value = 'FSSDAGETEQE'
        archive.AvatarDirectoryRouter.create_for_user(1)
        self.assertTrue(generate_mock.called)

    @base.mock.patch('src.central_files.archive.config.FILE_STORAGE_PATH', 'some/path')
    @base.mock.patch('src.central_files.archive.config.AVATAR_BUCKET_NAME', 'somename')
    @base.mock.patch('src.security.security_services.TokenService.generate')
    def test_should_return_instance(self, generate_mock):
        generate_mock.return_value = 'FSSDAGETEQE'
        avatar_directory_router = archive.AvatarDirectoryRouter.create_for_user(1)
        self.assertIsInstance(avatar_directory_router, archive.AvatarDirectoryRouter)
