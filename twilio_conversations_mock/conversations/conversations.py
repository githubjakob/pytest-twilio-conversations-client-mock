from twilio.base.exceptions import TwilioRestException

from constants import CONVERSATION_SID_PREFIX
from conversations.interfaces import ContextRessource, ListRessource, InstanceRessource
from conversations.messages import MessageList
from conversations.participants import ParticipantList
from data import data
from helper import create_sid


class ConversationContext(ContextRessource):
    def __init__(self, sid=None):
        self.sid = sid

    @property
    def participants(self) -> ParticipantList:
        return ParticipantList(self.sid)

    @property
    def messages(self) -> MessageList:
        return MessageList(conversation_sid=self.sid)

    def fetch(self):
        conversation = data["conversations"].get(self.sid)
        return ConversationInstance(conversation)

    def delete(self):
        conversation = data["conversations"].get(self.sid)

        if not conversation:
            raise TwilioRestException(status=404, uri="")

        del data["conversations"][self.sid]


class ConversationInstance(InstanceRessource):
    def __init__(self, payload):
        self._properties = {
            "sid": payload.get("sid"),
            "friendly_name": payload.get("friendly_name"),
            "attributes": payload.get("attributes"),
            # 'account_sid': payload.get('account_sid'),
            # 'chat_service_sid': payload.get('chat_service_sid'),
            # 'messaging_service_sid': payload.get('messaging_service_sid'),
            # 'unique_name': payload.get('unique_name'),
            # 'state': payload.get('state'),
            # 'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            # 'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            # 'timers': payload.get('timers'),
            # 'url': payload.get('url'),
            # 'links': payload.get('links'),
            # 'bindings': payload.get('bindings'),
        }

        self._context = None

    @property
    def _proxy(self) -> ConversationContext:
        """
        All actions of the Instance are proxied to the Context
        """

        if self._context is None:
            self._context = ConversationContext(self.sid)
        return self._context

    @property
    def messages(self) -> MessageList:
        return self._proxy.messages

    @property
    def participants(self) -> ParticipantList:
        return self._proxy.participants

    @property
    def sid(self) -> str:
        return self._properties.get("sid")

    @property
    def friendly_name(self) -> str:
        return self._properties.get("friendly_name")

    def delete(self):
        return self._proxy.delete()


class ConversationList(ListRessource):
    def __call__(self, sid=None) -> ConversationContext:
        return ConversationContext(sid)

    def get(self, sid) -> ConversationContext:
        return ConversationContext(sid)

    @property
    def messages(self, message_sid=None) -> MessageList:
        return MessageList(message_sid)

    def create(self, friendly_name=None) -> ConversationInstance:
        sid = create_sid(CONVERSATION_SID_PREFIX)
        conversation = {"sid": sid, "friendly_name": friendly_name}
        data["conversations"].update({sid: conversation})

        return ConversationInstance(conversation)

    def list(self):
        conversations = data["conversations"]
        return [ConversationInstance(c) for c in conversations.values()]
