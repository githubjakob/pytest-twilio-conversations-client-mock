from constants import MESSAGE_SID_PREFIX


def test_client_create_conversation(client):
    friendly_name = "Friendly Conversation"
    conversation = client.conversations.v1.conversations.create(
        friendly_name=friendly_name
    )
    assert conversation.sid is not None
    assert type(conversation.sid) is str
    assert conversation.sid.startswith("CH")
    assert conversation.friendly_name is not None
    assert type(conversation.friendly_name) is str
    assert conversation.friendly_name == friendly_name


def test_client_client_can_fetch_conversation(client):
    friendly_name = "Friendly Conversation"
    conversation = client.conversations.v1.conversations.create(
        friendly_name=friendly_name
    )

    sid = conversation.sid

    fetched_conversation = client.conversations.v1.conversations(sid).fetch()

    assert conversation.sid == fetched_conversation.sid
    assert conversation.friendly_name == fetched_conversation.friendly_name


def test_client_client_can_create_message(client):
    friendly_name = "Friendly Conversation"
    conversation = client.conversations.v1.conversations.create(
        friendly_name=friendly_name
    )

    messages = conversation.messages.list()

    assert messages is not None
    assert type(messages) is list
    assert len(messages) == 0

    body_1 = "My message 1"
    conversation.messages.create(body=body_1)

    messages = conversation.messages.list()
    assert len(messages) == 1
    message = messages[0]
    assert message.sid is not None
    assert type(message.sid) is str
    assert message.sid.startswith(MESSAGE_SID_PREFIX)
    assert message.body == body_1

    body_2 = "My message 2"
    conversation.messages.create(body=body_2)

    messages = conversation.messages.list()
    assert len(messages) == 2
    bodies = [m.body for m in messages]
    assert body_1 in bodies
    assert body_2 in bodies


def test_client_client_can_fetch_message_for_conversation(client):
    friendly_name = "Friendly Conversation"
    conversation = client.conversations.v1.conversations.create(
        friendly_name=friendly_name
    )

    body_1 = "My message 1"
    message = conversation.messages.create(body=body_1)

    assert message is not None
    assert message.sid is not None
    assert type(message.sid) is str
    assert message.sid.startswith(MESSAGE_SID_PREFIX)

    fetched_message = conversation.messages(message.sid).fetch()

    assert fetched_message is not None
    assert fetched_message.sid is not None

    assert message.sid == fetched_message.sid
    assert message.body == fetched_message.body


def test_client_can_list_conversation(client):
    friendly_name = "Friendly Conversation"
    client.conversations.v1.conversations.create(friendly_name=friendly_name)

    conversations = client.conversations.v1.conversations.list()

    assert conversations is not None
    assert type(conversations) is list
    assert len(conversations) == 1


def test_client_can_delete_conversation(client):
    friendly_name = "Friendly Conversation"
    conversation = client.conversations.v1.conversations.create(
        friendly_name=friendly_name
    )

    client.conversations.v1.conversations(conversation.sid).delete()
