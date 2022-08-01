from abc import ABC, abstractmethod

from constants import MESSAGE_SID_PREFIX
from conversations.conversations import ConversationList
from helper import create_sid


def setup_twilio_client_mock():
    class ParticipantMock:
        def __init__(self, conversation_sid):
            self.conversation_sid = conversation_sid
            self.identity = "default_identity"

    class ParticipantsMock:
        def __init__(self, conversation_sid):
            self.conversation_sid = conversation_sid

        def list(self):
            return [ParticipantMock(conversation_sid=self.conversation_sid)]

    class ConversationsClientV1Mock:
        @property
        def conversations(self):
            return ConversationList()

    class ConversationsClientMock:
        @property
        def v1(self):
            return ConversationsClientV1Mock()

    class ClientMock:
        @property
        def conversations(self):
            return ConversationsClientMock()

    return ClientMock()
