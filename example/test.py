from example.app import create_a_twilio_conversation


def test_create_a_twilio_conversation():

    conversation = create_a_twilio_conversation()

    assert conversation.sid is not None
    assert type(conversation.sid) is str
