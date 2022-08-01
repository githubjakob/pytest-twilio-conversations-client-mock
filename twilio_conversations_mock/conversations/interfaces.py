from abc import ABC


class ListRessource(ABC):
    def create(self, payload):
        raise NotImplementedError("Not implemented yet")

    def stream(self):
        raise NotImplementedError("Not implemented yet")

    def list(self):
        raise NotImplementedError("Not implemented yet")

    def page(self):
        raise NotImplementedError("Not implemented yet")

    def get_page(self):
        raise NotImplementedError("Not implemented yet")

    def get(self, sid):
        raise NotImplementedError("Not implemented yet")


class ContextRessource(ABC):
    def update(self):
        raise NotImplementedError("Not implemented yet")

    def delete(self):
        raise NotImplementedError("Not implemented yet")

    def fetch(self):
        raise NotImplementedError("Not implemented yet")


class InstanceRessource(ABC):
    def update(self):
        raise NotImplementedError("Not implemented yet")

    def delete(self):
        raise NotImplementedError("Not implemented yet")

    def fetch(self):
        raise NotImplementedError("Not implemented yet")
