class Action:
    def __init__(self, action_type, payload=None):
        self.action_type = action_type
        self.payload = payload or {}
