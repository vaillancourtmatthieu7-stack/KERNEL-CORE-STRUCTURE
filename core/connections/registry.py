class ConnectionRegistry:
    def __init__(self):
        self.connections = {}

    def register(self, name, connection):
        self.connections[name] = connection

    def get(self, name):
        return self.connections.get(name)
