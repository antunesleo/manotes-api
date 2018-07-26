import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app import config as config_module

config = config_module.get_config()


class Postman(object):

    @classmethod
    def send_confirmation_email(cls, name, from_address, to_address, subject):
        try:
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = "Notification: {}".format(subject)

            body = """
            Hello, {0}.
            This is a confirmation email.
            Welcome to manotes
            """.format(name)

            msg.attach(MIMEText(body, 'plain'))

            # server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
            server = smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT)
            server.starttls()
            # server.login("AKIAI6UTKEDROAOGB3UA", "AvFkgwarG6kzc2m98wiyZoPc6BavMyooazgUlbvQmdeP")
            server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
            text = msg.as_string()
            server.sendmail(from_address, to_address, text)
            server.quit()
        except Exception as ex:
            print(ex)
