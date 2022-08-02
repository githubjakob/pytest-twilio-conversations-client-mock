import os

import pytest
from twilio.rest import Client

from client import ClientMock

CLI_CLIENT_ARG_MOCK_ONLY = "mock"
CLI_CLIENT_ARG_TWILIO_CLIENT_ONLY = "twilio"

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

twilio_client = Client(account_sid, auth_token)
twilio_client_mock = ClientMock(account_sid, auth_token)

clients = [twilio_client, twilio_client_mock]


def pytest_addoption(parser):
    parser.addoption("--client", action="store", default="default name")


@pytest.fixture(scope="session")
def cli_client_arg(pytestconfig):
    return pytestconfig.getoption("client")


def cleanup_test_data(client):
    users = client.conversations.v1.users.list()
    for user in users:
        client.conversations.v1.users(user.identity).delete()

    conversations = client.conversations.v1.conversations.list()
    for conversation in conversations:
        client.conversations.v1.conversations(conversation.sid).delete()


@pytest.fixture(autouse=True, params=clients)
def client(request, cli_client_arg):
    if cli_client_arg == CLI_CLIENT_ARG_MOCK_ONLY:
        yield twilio_client_mock
        cleanup_test_data(twilio_client_mock)
    elif cli_client_arg == CLI_CLIENT_ARG_TWILIO_CLIENT_ONLY:
        yield twilio_client
        cleanup_test_data(twilio_client)
    else:
        yield request.param
        cleanup_test_data(request.param)
