class SnapshotManager:
    def capture(self, state):
        return dict(state)

    def restore(self, snapshot):
        return dict(snapshot)
