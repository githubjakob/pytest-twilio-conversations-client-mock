from unittest.mock import patch

from client import ClientMock

patch("twilio.rest.Client", return_value=ClientMock()).start()
