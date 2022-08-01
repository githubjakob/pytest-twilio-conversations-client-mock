import pytest
from twilio.rest import Client

from twilio_conversations_client_mock import setup_twilio_client_mock

account_sid = "AC03f054c9b284448bbfa04943fd6cb6c0"
auth_token = "65f61fb59b4dbb6d76fa468e977e48bc"

twilio_client = Client(account_sid, auth_token)

twilio_client_mock = setup_twilio_client_mock()

clients = [
    # twilio_client,
    twilio_client_mock
]


@pytest.fixture(autouse=True, params=clients)
def client(request):
    yield request.param
