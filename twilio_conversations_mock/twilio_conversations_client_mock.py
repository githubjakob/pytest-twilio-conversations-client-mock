from conversations.conversations import ConversationList
from conversations.users import UserList


def setup_twilio_client_mock():
    class ConversationsClientV1Mock:
        @property
        def conversations(self):
            return ConversationList()

        @property
        def users(self):
            return UserList()

    class ConversationsClientMock:
        @property
        def v1(self):
            return ConversationsClientV1Mock()

    class ClientMock:
        @property
        def conversations(self):
            return ConversationsClientMock()

    return ClientMock()
