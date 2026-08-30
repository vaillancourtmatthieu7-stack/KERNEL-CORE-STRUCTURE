from .world_state import KernelWorldState
from .snapshot import SnapshotManager
from .recovery import Recovery


class KernelCore:
    def __init__(self):
        self.tick_count = 0
        self.simulation_time = 0.0

        self.world = KernelWorldState()
        self.snapshot_manager = SnapshotManager()
        self.recovery_manager = Recovery()

    def tick(self, delta_time: float = 1.0):
        dt = float(delta_time)

        self.world.step(dt)

        self.tick_count += 1
        self.simulation_time += dt

        return self.snapshot()

    def observe(self):
        return self.snapshot()

    def snapshot(self):
        state = {
            "tick": self.tick_count,
            "time": self.simulation_time,
            "simulation_time": self.simulation_time,
            "entities": self.world.snapshot()["entities"],
        }

        return self.snapshot_manager.capture(state)

    def recovery(self, snapshot):
        restored = self.recovery_manager.load(snapshot)

        self.tick_count = int(restored.get("tick", 0))
        self.simulation_time = float(
            restored.get(
                "simulation_time",
                restored.get("time", 0.0)
            )
        )

        self.world.restore(restored)

        return self.snapshot()
