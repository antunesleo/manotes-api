import os
from tests import base
from src import config
from src import exceptions


class ConfigTest(base.TestCase):

    def setUp(self):
        super(ConfigTest, self).setUp()
        self.config = config.Config()

    def test_has_DEBUG(self):
        self.assertTrue(hasattr(self.config, 'DEBUG'))

    def test_has_DEBUG_default_false(self):
        self.assertFalse(self.config.DEBUG)

    def test_has_TESTING(self):
        self.assertTrue(hasattr(self.config, 'TESTING'))

    def test_has_TESTING_default_false(self):
        self.assertFalse(self.config.TESTING)

    def test_has_DEVELOPMENT(self):
        self.assertTrue(hasattr(self.config, 'DEVELOPMENT'))

    def test_has_DEVELOPMENT_default_false(self):
        self.assertFalse(self.config.DEVELOPMENT)

    def test_has_ENVIRONMENT(self):
        self.assertTrue(hasattr(self.config, 'ENVIRONMENT'))

    def test_has_ENVIRONMENT_default_development(self):
        self.assertEqual(self.config.ENVIRONMENT, 'development')

    def test_has_SQLALCHEMY_DATABASE_URI(self):
        self.assertTrue(hasattr(self.config, 'SQLALCHEMY_DATABASE_URI'))

    def test_has_SQLALCHEMY_DATABASE_URI_from_environment(self):
        self.assertEqual(self.config.SQLALCHEMY_DATABASE_URI, os.environ['DATABASE_URL'])

    def test_has_PORT(self):
        self.assertTrue(hasattr(self.config, 'PORT'))

    def test_has_PORT_from_environment(self):
        self.assertEqual(self.config.PORT, os.environ['PORT'])

    def test_has_REDIS_URL(self):
        self.assertTrue(hasattr(self.config, 'REDIS_URL'))

    def test_has_REDIS_URL_from_environment(self):
        self.assertEqual(self.config.REDIS_URL, os.environ['REDIS_URL'])

    def test_has_SMTP_HOST(self):
        self.assertTrue(hasattr(self.config, 'SMTP_HOST'))

    def test_has_SMTP_HOST_from_environment(self):
        self.assertEqual(self.config.SMTP_HOST, os.environ['SMTP_HOST'])

    def test_has_SMTP_PORT(self):
        self.assertTrue(hasattr(self.config, 'SMTP_PORT'))

    def test_has_SMTP_PORT_from_environment(self):
        self.assertEqual(self.config.SMTP_PORT, os.environ['SMTP_PORT'])

    def test_has_SMTP_USERNAME(self):
        self.assertTrue(hasattr(self.config, 'SMTP_USERNAME'))

    def test_has_SMTP_USERNAME_from_environment(self):
        self.assertEqual(self.config.SMTP_USERNAME, os.environ['SMTP_USERNAME'])

    def test_has_SMTP_PASSWORD(self):
        self.assertTrue(hasattr(self.config, 'SMTP_PASSWORD'))

    def test_has_SMTP_PASSWORD_from_environment(self):
        self.assertEqual(self.config.SMTP_PASSWORD, os.environ['SMTP_PASSWORD'])

    def test_has_FILE_STORAGE_PATH(self):
        self.assertTrue(hasattr(self.config, 'FILE_STORAGE_PATH'))

    def test_has_FILE_STORAGE_PATH_from_environment(self):
        self.assertEqual(self.config.FILE_STORAGE_PATH, os.environ['FILE_STORAGE_PATH'])

    def test_has_AVATAR_BUCKET_NAME(self):
        self.assertTrue(hasattr(self.config, 'AVATAR_BUCKET_NAME'))

    def test_has_AVATAR_BUCKET_NAME_from_environment(self):
        self.assertEqual(self.config.AVATAR_BUCKET_NAME, os.environ['AVATAR_BUCKET_NAME'])

    def test_has_S3_AWS_ACCESS_KEY_ID(self):
        self.assertTrue(hasattr(self.config, 'S3_AWS_ACCESS_KEY_ID'))

    def test_has_S3_AWS_ACCESS_KEY_ID_from_environment(self):
        self.assertEqual(self.config.S3_AWS_ACCESS_KEY_ID, os.environ['S3_AWS_ACCESS_KEY_ID'])

    def test_has_S3_AWS_SECRET_ACCESS_KEY(self):
        self.assertTrue(hasattr(self.config, 'S3_AWS_SECRET_ACCESS_KEY'))

    def test_has_S3_AWS_SECRET_ACCESS_KEY_from_environment(self):
        self.assertEqual(self.config.S3_AWS_SECRET_ACCESS_KEY, os.environ['S3_AWS_SECRET_ACCESS_KEY'])

    def test_has_TEMP_PATH(self):
        self.assertTrue(hasattr(self.config, 'TEMP_PATH'))

    def test_has_TEMP_PATH_from_environment(self):
        self.assertEqual(self.config.TEMP_PATH, os.environ['TEMP_PATH'])


class ProductionConfigTest(base.TestCase):

    def setUp(self):
        super(ProductionConfigTest, self).setUp()
        self.config = config.ProductionConfig()

    def test_has_PRODUCTION(self):
        self.assertTrue(hasattr(self.config, 'PRODUCTION'))

    def test_has_PRODUCTION_default_true(self):
        self.assertTrue(self.config.PRODUCTION)


class DevelopmentConfigTest(base.TestCase):

    def setUp(self):
        super(DevelopmentConfigTest, self).setUp()
        self.config = config.DevelopmentConfig()

    def test_has_DEBUG(self):
        self.assertTrue(hasattr(self.config, 'DEBUG'))

    def test_has_DEBUG_default_true(self):
        self.assertTrue(self.config.DEBUG)

    def test_has_DEVELOPMENT(self):
        self.assertTrue(hasattr(self.config, 'DEVELOPMENT'))

    def test_has_DEVELOPMENT_default_true(self):
        self.assertTrue(self.config.DEVELOPMENT)

    def test_has_SQLALCHEMY_RECORD_QUERIES(self):
        self.assertTrue(hasattr(self.config, 'SQLALCHEMY_RECORD_QUERIES'))

    def test_has_SQLALCHEMY_RECORD_QUERIES_default_true(self):
        self.assertTrue(self.config.SQLALCHEMY_DATABASE_URI)


class TestingConfigTest(base.TestCase):

    def setUp(self):
        super(TestingConfigTest, self).setUp()
        self.config = config.TestingConfig()

    def test_has_TESTING(self):
        self.assertTrue(hasattr(self.config, 'TESTING'))

    def test_has_TESTING_default_true(self):
        self.assertTrue(self.config.TESTING)

    def test_has_KEY_ON_TEST(self):
        self.assertTrue(hasattr(self.config, 'KEY_ON_TEST'))

    def test_has_KEY_ON_TEST_default_KEY_ON_TEST(self):
        self.assertEqual(self.config.KEY_ON_TEST, 'KEY ON TEST')

    def test_has_ENVIRONMENT(self):
        self.assertTrue(hasattr(self.config, 'ENVIRONMENT'))

    def test_has_ENVIRONMENT_default_test(self):
        self.assertEqual(self.config.ENVIRONMENT, 'test')


class GetConfigTest(base.TestCase):

    @base.mock.patch('src.config.import_module')
    def test_should_call_import_module_to_import_config_module(self, import_module_mock):
        config.get_config()
        self.assertTrue(import_module_mock.called)

    @base.mock.patch('src.config.import_module')
    def test_should_raise_config_class_not_found_if_config_class_is_none(self, import_module_mock):
        config_module_mock = self.mock.MagicMock()
        config_module_mock.TestingConfig = None
        import_module_mock.return_value = config_module_mock
        with self.assertRaises(exceptions.ConfigClassNotFound):
            config.get_config()

    @base.mock.patch('src.config.import_module')
    def test_should_return_config_class_if_config_class(self, import_module_mock):
        config_module_mock = self.mock.MagicMock()
        testing_config_mock = self.mock.MagicMock()
        config_module_mock.TestingConfig = testing_config_mock
        import_module_mock.return_value = config_module_mock
        testing_config = config.get_config()
        self.assertEqual(testing_config, testing_config_mock)
