from constants import PARTICIPANT_SID_PREFIX


def test_conversations_have_participants(client):
    conversation = client.conversations.v1.conversations.create()
    participants = conversation.participants.list()
    assert participants is not None
    assert type(participants) is list
    assert len(participants) == 0


def test_client_can_create_participant(client):
    identity = "test identity"
    conversation = client.conversations.v1.conversations.create()
    participant = conversation.participants.create(identity=identity)
    assert participant is not None
    assert participant.identity == identity


def test_client_can_list_participants(client):
    identity = "test identity"
    conversation = client.conversations.v1.conversations.create()
    conversation.participants.create(identity=identity)
    participants = conversation.participants.list()
    assert participants is not None
    assert type(participants) is list
    assert len(participants) == 1
    participant = participants[0]
    assert participant.identity == identity
    assert type(participant.sid) is str
    assert participant.sid.startswith(PARTICIPANT_SID_PREFIX)
