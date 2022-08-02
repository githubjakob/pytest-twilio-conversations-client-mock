from unittest.mock import patch

from twilio_conversations_mock.client import ClientMock

patch("twilio.rest.Client", return_value=ClientMock()).start()
