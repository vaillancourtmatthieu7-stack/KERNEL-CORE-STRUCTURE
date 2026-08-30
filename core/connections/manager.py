from .registry import ConnectionRegistry


class ConnectionManager:
    def __init__(self):
        self.registry = ConnectionRegistry()

    def register(self, name, adapter):
        self.registry.register(name, adapter)

    def get(self, name):
        return self.registry.get(name)
