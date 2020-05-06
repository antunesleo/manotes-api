from tests.unit import base
from src.async_tasks import tasks


class StartSendEmailTest(base.TestCase):

    @base.mock.patch('src.async_tasks.tasks.send_email.apply_async', base.mock.MagicMock())
    @base.mock.patch('src.async_tasks.tasks.establish.logger.info')
    def test_should_call_establish_logger_to_info(self, info_mock):
        tasks.start_send_email('name', 'from_address', 'to_address', 'subject')
        self.assertTrue(info_mock.called)

    @base.mock.patch('src.async_tasks.tasks.establish.logger.info', base.mock.MagicMock())
    @base.mock.patch('src.async_tasks.tasks.send_email.apply_async')
    def test_should_apply_async_in_send_email(self, apply_async_mock):
        name = 'name'
        from_address = 'from_address'
        to_address = 'to_address'
        subject = 'subject'
        tasks.start_send_email(name, from_address, to_address, subject)
        apply_async_mock.assert_called_with((name, from_address, to_address, subject))

    @base.mock.patch('src.async_tasks.tasks.establish.logger.info', base.mock.MagicMock())
    @base.mock.patch('src.async_tasks.tasks.send_email.apply_async')
    def test_should_return_task_id(self, apply_async_mock):
        task_mock = self.mock.MagicMock()
        task_mock.id = 1
        apply_async_mock.return_value = task_mock
        task_id = tasks.start_send_email('name', 'from_address', 'to_address', 'subject')
        self.assertEqual(task_id, 1)


class SendEmailTest(base.TestCase):

    @base.mock.patch('src.async_tasks.tasks.postman.Postman.send_confirmation_email')
    def test_should_call_postman_to_send_confirmation_email(self, send_confirmation_email_mock):
        tasks.send_email('name', 'from_address', 'to_address', 'subject')
        send_confirmation_email_mock.assert_called_with('name', 'from_address', 'to_address', 'subject')
