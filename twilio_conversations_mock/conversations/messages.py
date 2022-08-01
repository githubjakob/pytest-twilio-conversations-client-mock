from constants import MESSAGE_SID_PREFIX
from conversations.interfaces import ContextRessource, ListRessource
from data import data
from helper import create_sid


class MessageInstance:
    def __init__(self, message_sid, conversation_sid, body):
        self.sid = message_sid
        self.conversation_sid = conversation_sid
        self.attributes = {}
        self.body = body

    def update(self, *args, **kwargs):
        pass


class MessageContext(ContextRessource):
    def __init__(self, conversation_sid, sid):
        self.sid = sid
        self.conversation_sid = conversation_sid

    def fetch(self) -> MessageInstance:
        conversation = data["conversations"].get(self.conversation_sid)
        messages = conversation["messages"]
        message = messages.get(self.sid)
        return MessageInstance(message["sid"], self.conversation_sid, message["body"])


class MessageList(ListRessource):
    def __init__(self, conversation_sid):
        self.conversation_sid = conversation_sid

    def __call__(self, message_sid=None):
        return MessageContext(self.conversation_sid, message_sid)

    def fetch(self):
        return MessageInstance(self.message_sid, self.conversation_sid)

    def list(self):
        conversation = data["conversations"].get(self.conversation_sid)
        messages = conversation.get("messages", {})
        return [
            MessageInstance(m["sid"], self.conversation_sid, m["body"])
            for m in messages.values()
        ]

    def create(self, body) -> MessageInstance:
        conversation = data["conversations"].get(self.conversation_sid)
        if not conversation.get("messages"):
            conversation.update({"messages": {}})

        sid = create_sid(MESSAGE_SID_PREFIX)
        conversation["messages"].update({sid: {"sid": sid, "body": body}})

        return MessageInstance(sid, self.conversation_sid, body)
