class WorldAdapter:
    adapter_type = "world"

    def capabilities(self):
        return ["world"]

    def connect(self):
        return True

    def disconnect(self):
        return True
