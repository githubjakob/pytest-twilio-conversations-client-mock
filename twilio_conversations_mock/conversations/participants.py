from constants import PARTICIPANT_SID_PREFIX
from conversations.interfaces import ContextRessource, ListRessource
from data import data
from helper import create_sid


class ParticipantInstance:
    def __init__(self, payload):
        self._properties = {
            "conversation_sid": payload.get("conversation_sid"),
            "sid": payload.get("sid"),
            "identity": payload.get("identity"),
        }

        self._context = None

    def _proxy(self):
        if self._context is None:
            self._context = ParticipantContext(
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
    def identity(self):
        return self._properties["identity"]

    def update(self, *args, **kwargs):
        pass


class ParticipantContext(ContextRessource):
    def __init__(self, conversation_sid, sid):
        self.sid = sid
        self.conversation_sid = conversation_sid

    def fetch(self) -> ParticipantInstance:
        conversation = data["conversations"].get(self.conversation_sid)
        participants = conversation["participants"]
        participant = participants.get(self.sid)
        return ParticipantInstance(participant)


class ParticipantList(ListRessource):
    def __init__(self, conversation_sid):
        self.conversation_sid = conversation_sid

    def __call__(self, sid=None):
        return ParticipantContext(self.conversation_sid, sid)

    def list(self):
        conversation = data["conversations"].get(self.conversation_sid)
        participants = conversation.get("participants", {})
        return [ParticipantInstance(p) for p in participants.values()]

    def create(self, identity) -> ParticipantInstance:
        conversation = data["conversations"].get(self.conversation_sid)
        if not conversation.get("participants"):
            conversation.update({"participants": {}})

        sid = create_sid(PARTICIPANT_SID_PREFIX)
        participant = {
            "sid": sid,
            "conversation_sid": self.conversation_sid,
            "identity": identity,
        }
        conversation["participants"].update({sid: participant})

        return ParticipantInstance(participant)
