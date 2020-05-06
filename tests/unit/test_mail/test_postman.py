from src.mail import postman
from tests.unit import base

from src import config as config_module

config = config_module.get_config()


class PostmanSendConfirmationEmailTest(base.TestCase):

    @base.mock.patch('src.mail.postman.MIMEMultipart')
    @base.mock.patch('src.mail.postman.smtplib')
    def test_should_instantiate_mime_multipart(self, smtplib_mock, mime_multipart_mock):
        postman.Postman.send_confirmation_email('breno', 'breno@manotes.com', 'a@manotes.com', 'How do you eim?')
        self.assertTrue(mime_multipart_mock.called)

    @base.mock.patch('src.mail.postman.MIMEText')
    @base.mock.patch('src.mail.postman.MIMEMultipart')
    @base.mock.patch('src.mail.postman.smtplib')
    def test_should_call_mime_text_with_body_and_plain(self, smtplib_mock, mime_multipart_mock, mime_text):
        postman.Postman.send_confirmation_email('Breno', 'breno@manotes.com', 'a@manotes.com', 'How do you eim?')
        body = """
            Hello, {0}.
            This is a confirmation email.
            Welcome to manotes
            """.format('Breno')
        mime_text.assert_called_with(body, 'plain')

    @base.mock.patch('src.mail.postman.MIMEText')
    @base.mock.patch('src.mail.postman.MIMEMultipart')
    @base.mock.patch('src.mail.postman.smtplib')
    def test_should_call_msg_to_attach_mime_text(self, smtplib_mock, mime_multipart_mock, mime_text):
        msg_mock = self.mock.MagicMock()
        mime_multipart_mock.return_value = msg_mock
        mime_text_instance_mock = self.mock.MagicMock
        mime_text.return_value = mime_text_instance_mock
        postman.Postman.send_confirmation_email('Breno', 'breno@manotes.com', 'a@manotes.com', 'How do you eim?')
        msg_mock.attach.assert_called_with(mime_text_instance_mock)

    @base.mock.patch('src.mail.postman.MIMEText')
    @base.mock.patch('src.mail.postman.MIMEMultipart')
    @base.mock.patch('src.mail.postman.smtplib')
    def test_should_call_smtplib_to_instatiate_smtp(self, smtplib_mock, mime_multipart_mock, mime_text):
        postman.Postman.send_confirmation_email('Breno', 'breno@manotes.com', 'a@manotes.com', 'How do you eim?')
        smtplib_mock.SMTP.assert_called_with(config.SMTP_HOST, config.SMTP_PORT)

    @base.mock.patch('src.mail.postman.MIMEText')
    @base.mock.patch('src.mail.postman.MIMEMultipart')
    @base.mock.patch('src.mail.postman.smtplib')
    def test_should_call_server_to_starttls(self, smtplib_mock, mime_multipart_mock, mime_text):
        server_mock = self.mock.MagicMock()
        smtplib_mock.SMTP.return_value = server_mock
        postman.Postman.send_confirmation_email('Breno', 'breno@manotes.com', 'a@manotes.com', 'How do you eim?')
        self.assertTrue(server_mock.starttls.called)

    @base.mock.patch('src.mail.postman.MIMEText')
    @base.mock.patch('src.mail.postman.MIMEMultipart')
    @base.mock.patch('src.mail.postman.smtplib')
    def test_should_call_server_to_login(self, smtplib_mock, mime_multipart_mock, mime_text):
        server_mock = self.mock.MagicMock()
        smtplib_mock.SMTP.return_value = server_mock
        postman.Postman.send_confirmation_email('Breno', 'breno@manotes.com', 'a@manotes.com', 'How do you eim?')
        server_mock.login.assert_called_with(config.SMTP_USERNAME, config.SMTP_PASSWORD)

    @base.mock.patch('src.mail.postman.MIMEText')
    @base.mock.patch('src.mail.postman.MIMEMultipart')
    @base.mock.patch('src.mail.postman.smtplib')
    def test_should_call_msg_to_as_string(self, smtplib_mock, mime_multipart_mock, mime_text):
        msg_mock = self.mock.MagicMock()
        mime_multipart_mock.return_value = msg_mock
        mime_text_instance_mock = self.mock.MagicMock
        mime_text.return_value = mime_text_instance_mock
        postman.Postman.send_confirmation_email('Breno', 'breno@manotes.com', 'a@manotes.com', 'How do you eim?')
        self.assertTrue(msg_mock.as_string.called)

    @base.mock.patch('src.mail.postman.MIMEText')
    @base.mock.patch('src.mail.postman.MIMEMultipart')
    @base.mock.patch('src.mail.postman.smtplib')
    def test_should_call_server_to_sendmail(self, smtplib_mock, mime_multipart_mock, mime_text):
        msg_mock = self.mock.MagicMock()
        msg_mock.as_string.return_value = 'AAA'
        mime_multipart_mock.return_value = msg_mock
        server_mock = self.mock.MagicMock()
        smtplib_mock.SMTP.return_value = server_mock
        postman.Postman.send_confirmation_email('Breno', 'breno@manotes.com', 'a@manotes.com', 'How do you eim?')
        server_mock.sendmail.assert_called_with('breno@manotes.com', 'a@manotes.com', 'AAA')

    @base.mock.patch('src.mail.postman.MIMEText')
    @base.mock.patch('src.mail.postman.MIMEMultipart')
    @base.mock.patch('src.mail.postman.smtplib')
    def test_should_call_server_to_quit(self, smtplib_mock, mime_multipart_mock, mime_text):
        server_mock = self.mock.MagicMock()
        smtplib_mock.SMTP.return_value = server_mock
        postman.Postman.send_confirmation_email('Breno', 'breno@manotes.com', 'a@manotes.com', 'How do you eim?')
        self.assertTrue(server_mock.quit.called)
