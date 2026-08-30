class SimulationAdapter:
    adapter_type = "simulation"

    def capabilities(self):
        return ["simulation"]

    def connect(self):
        return True

    def disconnect(self):
        return True
