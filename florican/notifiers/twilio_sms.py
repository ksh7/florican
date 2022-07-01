import logging

from .base import BaseNotifier


__all__ = ["TwilioSMSNotifier"]


class TwilioSMSNotifier(BaseNotifier):
    """A twilio_sms notifier."""

    TYPE = "twilio_sms"

    def __init__(self, account_sid: str, auth_token: str, msg_to: str, msg_from: str):
        try:
            from twilio.rest import Client
        except ModuleNotFoundError:
            logging.error("Please install the `twilio` package.")
            exit(1)

        self._msg_to = msg_to
        self._msg_from = msg_from
        self._client = Client(account_sid, auth_token)

    def notify(self, text: str) -> None:
        """Sends a message."""
        self._client.messages.create(to=self._msg_to, from_=self._msg_from, body=text)
