from constants import MESSAGE_SID_PREFIX
from conversations.interfaces import ContextRessource, ListRessource
from data import data
from helper import create_sid


class MessageInstance:
    def __init__(self, payload):
        self._properties = {
            "conversation_sid": payload.get("conversation_sid"),
            "sid": payload.get("sid"),
            "attributes": payload.get("attributes"),
            "body": payload.get("body"),
            "author": payload.get("author"),
            # 'account_sid': payload.get('account_sid'),
            # 'index': deserialize.integer(payload.get('index')),
            # 'media': payload.get('media'),
            # 'participant_sid': payload.get('participant_sid'),
            # 'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            # 'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            # 'url': payload.get('url'),
            # 'delivery': payload.get('delivery'),
            # 'links': payload.get('links'),
        }

        self._context = None

    def _proxy(self):
        if self._context is None:
            self._context = MessageContext(
                conversation_sid=self._properties["conversation_sid"],
                sid=self._properties["sid"],
            )
        return self._context

    @property
    def conversation_sid(self):
        return self._properties["conversation_sid"]

    @property
    def sid(self):
        return self._properties["sid"]

    @property
    def body(self):
        return self._properties["body"]

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
        return MessageInstance(message)


class MessageList(ListRessource):
    def __init__(self, conversation_sid):
        self.conversation_sid = conversation_sid

    def __call__(self, sid=None):
        return MessageContext(self.conversation_sid, sid)

    def list(self):
        conversation = data["conversations"].get(self.conversation_sid)
        messages = conversation.get("messages", {})
        return [MessageInstance(m) for m in messages.values()]

    def create(self, body) -> MessageInstance:
        conversation = data["conversations"].get(self.conversation_sid)
        if not conversation.get("messages"):
            conversation.update({"messages": {}})

        sid = create_sid(MESSAGE_SID_PREFIX)
        massage = {"sid": sid, "conversation_sid": self.conversation_sid, "body": body}
        conversation["messages"].update({sid: massage})

        return MessageInstance(massage)
