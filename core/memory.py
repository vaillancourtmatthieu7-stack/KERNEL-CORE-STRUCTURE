class Memory:
    def __init__(self):
        self.state = {}
        self.persistent = {}

    def read(self, key, default=None):
        return self.state.get(key, default)

    def write(self, key, value):
        self.state[key] = value
