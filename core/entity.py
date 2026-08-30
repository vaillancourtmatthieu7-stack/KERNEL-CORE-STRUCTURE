from dataclasses import dataclass, field
from typing import List


@dataclass
class Entity:
    name: str
    position: List[float] = field(default_factory=lambda: [0.0, 0.0, 0.0])
    velocity: List[float] = field(default_factory=lambda: [0.0, 0.0, 0.0])

    def __post_init__(self):
        self.position = [float(x) for x in self.position]
        self.velocity = [float(x) for x in self.velocity]

        if len(self.position) != 3:
            raise ValueError("position doit contenir 3 coordonnées")

        if len(self.velocity) != 3:
            raise ValueError("velocity doit contenir 3 coordonnées")

    def step(self, delta_time: float):
        dt = float(delta_time)

        self.position = [
            self.position[i] + self.velocity[i] * dt
            for i in range(3)
        ]

    def snapshot(self):
        return {
            "name": self.name,
            "position": list(self.position),
            "velocity": list(self.velocity),
        }

    @classmethod
    def from_snapshot(cls, data):
        return cls(
            data["name"],
            position=list(data["position"]),
            velocity=list(data["velocity"]),
        )
