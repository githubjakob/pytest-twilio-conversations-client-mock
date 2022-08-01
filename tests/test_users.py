import pytest
from twilio.base.exceptions import TwilioRestException


def test_client_can_create_user(client):
    identity = "test identity"
    client.conversations.v1.users.create(identity=identity)


def test_client_creating_user_twice_throws_exception(client):
    identity = "test identity"
    client.conversations.v1.users.create(identity=identity)
    with pytest.raises(TwilioRestException):
        client.conversations.v1.users.create(identity=identity)


def test_client_can_list_users(client):
    users = client.conversations.v1.users.list()
    assert users is not None
    assert type(users) is list
    assert len(users) == 0


def test_list_users_returns_created_user(client):
    identity = "test identity"
    client.conversations.v1.users.create(identity=identity)

    users = client.conversations.v1.users.list()

    assert users is not None
    assert type(users) is list
    assert len(users) == 1
    user = users[0]
    assert user.identity == identity

    identity2 = "test identity2"

    client.conversations.v1.users.create(identity=identity2)

    users = client.conversations.v1.users.list()
    assert users is not None
    assert type(users) is list
    assert len(users) == 2
    identities = [u.identity for u in users]
    assert identity in identities
    assert identity2 in identities


def test_when_user_does_not_exist_delete_throws_exception(client):
    identity = "non existing user identity"
    with pytest.raises(TwilioRestException):
        client.conversations.v1.users(identity).delete()


def test_client_can_delete_user(client):
    identity = "test identity"
    client.conversations.v1.users.create(identity=identity)
    client.conversations.v1.users(identity).delete()


def test_fetching_non_existing_user_throws_exception(client):
    identity = "test identity"
    with pytest.raises(TwilioRestException):
        client.conversations.v1.users(identity).fetch()


def test_client_can_fetch_existing_user(client):
    identity = "test identity"
    client.conversations.v1.users.create(identity=identity)
    user = client.conversations.v1.users(identity).fetch()
    assert user is not None
    assert user.identity == identity


def test_deleted_user_does_not_exist_anymore(client):
    identity = "test identity"
    client.conversations.v1.users.create(identity=identity)
    client.conversations.v1.users(identity).delete()
    with pytest.raises(TwilioRestException):
        client.conversations.v1.users(identity).fetch()
