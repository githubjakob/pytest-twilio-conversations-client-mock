from example.app import create_a_twilio_conversation, fetch_a_twilio_conversation


def test_testing_the_mock():

    conversation = create_a_twilio_conversation()

    assert conversation.sid is not None
    assert type(conversation.sid) is str

    fetched_conversation = fetch_a_twilio_conversation(conversation.sid)

    assert conversation.sid == fetched_conversation.sid
