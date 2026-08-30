class Recovery:
    def save(self, state):
        return dict(state)

    def load(self, snapshot):
        return dict(snapshot)
