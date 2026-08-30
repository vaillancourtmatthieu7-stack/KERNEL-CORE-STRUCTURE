class Intent:
    def __init__(self, intent_type, payload=None):
        self.intent_type = intent_type
        self.payload = payload or {}
