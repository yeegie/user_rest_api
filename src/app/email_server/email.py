from .base import BaseEmailService
from logging import Logger


class EmailService(BaseEmailService):
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    async def notify(self, message: str, recipient: str):
        self._logger.info(f"Message sended to {recipient} f({message})")

    def send_code(self, recipient: str, code: str) -> None:
        self._logger.info(f"Message with code ({code}) sended to {recipient}")
