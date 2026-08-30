from .entity import Entity


class KernelWorldState:
    def __init__(self):
        self.entities = {}

    def add_entity(self, entity: Entity):
        if not isinstance(entity, Entity):
            raise TypeError("entity doit être une instance de Entity")

        self.entities[entity.name] = entity
        return entity

    def remove_entity(self, name):
        return self.entities.pop(name, None)

    def get_entity(self, name):
        return self.entities.get(name)

    def step(self, delta_time: float):
        for entity in self.entities.values():
            entity.step(delta_time)

    def snapshot(self):
        return {
            "entities": {
                name: entity.snapshot()
                for name, entity in self.entities.items()
            }
        }

    def restore(self, snapshot):
        self.entities = {
            name: Entity.from_snapshot(data)
            for name, data in snapshot.get("entities", {}).items()
        }
        return self
