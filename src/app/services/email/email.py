from .base import BaseEmailService


class EmailService(BaseEmailService):
    def send_welcome_message(self, recipient: str) -> None:
        print("Hello, this is welcome message.")

    def send_code(sef, recipient: str, code: str) -> None:
        print(f"Hello, your code: {code}")
