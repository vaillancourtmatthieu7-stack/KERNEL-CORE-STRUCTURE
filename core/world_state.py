class KernelWorldState:
    def __init__(self):
        self.entities = {}

    def snapshot(self):
        return {
            "entities": dict(self.entities),
        }
