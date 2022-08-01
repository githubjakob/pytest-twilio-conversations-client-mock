from conversations.interfaces import ContextRessource, ListRessource
from conversations.messages import MessageList
from conversations.participants import ParticipantList
from data import data
from helper import create_sid


class ConversationContext(ContextRessource):
    def __init__(self, conversation_sid=None, friendly_name=None):
        self.friendly_name = None
        self.sid = conversation_sid
        self.friendly_name = friendly_name

    @property
    def participants(self) -> ParticipantList:
        return ParticipantList(self.sid)

    @property
    def messages(self) -> MessageList:
        return MessageList(conversation_sid=self.sid)

    def fetch(self):
        conversation = data["conversations"].get(self.sid)
        return ConversationList(conversation["sid"], conversation["friendly_name"])


class ConversationInstance:
    def __init__(self, conversation_sid=None, friendly_name=None):
        self.sid = conversation_sid
        self.friendly_name = friendly_name

        self._context = None

    @property
    def _proxy(self) -> ConversationContext:
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        """

        if self._context is None:
            self._context = ConversationContext(self.sid, self.friendly_name)
        return self._context

    @property
    def messages(self) -> MessageList:
        return self._proxy.messages

    @property
    def participants(self) -> ParticipantList:
        return self._proxy.participants


class ConversationList(ListRessource):
    def __init__(self, conversation_sid=None, friendly_name=None):
        self.friendly_name = None
        self.sid = conversation_sid
        self.friendly_name = friendly_name

    def __call__(self, conversation_sid=None) -> ConversationContext:
        return ConversationContext(conversation_sid)

    def get(self) -> ConversationContext:
        pass

    @property
    def messages(self, message_sid=None) -> MessageList:
        return MessageList(message_sid, self.sid)

    def create(self, friendly_name=None) -> ConversationInstance:
        sid = create_sid("CH")
        data["conversations"].update(
            {sid: {"sid": sid, "friendly_name": friendly_name}}
        )

        self.friendly_name = friendly_name
        self.sid = sid
        return ConversationInstance(sid, friendly_name)
