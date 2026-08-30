class ConnectionAdapter:
    adapter_type = "generic"

    def capabilities(self):
        return []

    def connect(self):
        return True

    def disconnect(self):
        return True
