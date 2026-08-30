class KernelCore:
    def __init__(self):
        self.tick_count = 0
        self.simulation_time = 0.0

    def tick(self, delta_time: float = 1.0):
        self.tick_count += 1
        self.simulation_time += float(delta_time)
        return self.snapshot()

    def observe(self):
        return self.snapshot()

    def snapshot(self):
        return {
            "tick": self.tick_count,
            "time": self.simulation_time,
        }
