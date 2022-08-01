def test_client_is_not_none(client):
    assert client is not None
    assert client.conversations is not None
    assert client.conversations.v1 is not None
    assert client.conversations.v1.conversations is not None
    assert client.conversations.v1.users is not None
