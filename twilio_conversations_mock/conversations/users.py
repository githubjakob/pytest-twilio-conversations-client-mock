from twilio.base.exceptions import TwilioRestException

from conversations.interfaces import ListRessource, ContextRessource
from data import data


class UserInstance:
    def __init__(self, identity):
        self.identity = identity


class UserContext(ContextRessource):
    def __init__(self, identity):
        self.identity = identity

    def delete(self):
        users = data["users"]
        user = users.get(self.identity)
        if not user:
            raise TwilioRestException(status=404, uri="")

        del users[self.identity]

    def fetch(self):
        users = data["users"]
        user = users.get(self.identity)
        if not user:
            raise TwilioRestException(status=404, uri="")

        return UserInstance(user["identity"])


class UserList(ListRessource):
    def create(self, identity) -> UserInstance:
        users = data["users"]
        user = users.get(identity)
        if user:
            raise TwilioRestException(status=409, uri="")

        users.update({identity: {"identity": identity}})
        return UserInstance(identity=identity)

    def list(self):
        users = data["users"]
        return [UserInstance(identity=u["identity"]) for u in users.values()]

    def __call__(self, identity=None):
        return UserContext(identity)
