__all__ = [
    "EmailServer"
]

from logging import Logger
from app.factories.config.config_schemas import EmailSettings

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailServer():
    def __init__(
        self,
        logger: Logger,
        config: EmailSettings
    ) -> None:
        self.__logger = logger
        self.__config = config
        self.__server = None

    def connect(self):
        try:
            # Connection
            self.__server = smtplib.SMTP(
                self.__config.host,
                self.__config.port,
            )

            # Tls
            if self.__config.tls:
                self.__server.starttls()

            # Login
            self.__server.login(
                self.__config.email_from,
                self.__config.password.get_secret_value(),
            )

            self.__logger.info("Email server is runned")
        except Exception as ex:
            self.__logger.error("Failed to connect email server.")
            self.__server = None

    def disconnect(self):
        if self.server:
            self.server.quit()
            print("Disconnected from the SMTP server.")
        else:
            print("No active server connection to close.")

    def send_email(self, recipient: str, subject: str, body: str):
        if not self.server:
            self.__logger.error("Not connected to the server.")
            return
        
        msg = MIMEMultipart()
        msg['From'] = self.__config.email_from
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            self.server.sendmail(self.__config.email_from, recipient, msg.as_string())
        except Exception as e:
            self.__logger.error(f"Failed to send email: {e}")
