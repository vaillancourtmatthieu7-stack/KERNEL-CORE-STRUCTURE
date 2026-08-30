class Agent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.state = "idle"

    def perceive(self, observation):
        return observation

    def decide(self, observation):
        return {"type": "observe", "agent": self.agent_id}

    def act(self, action):
        return action
