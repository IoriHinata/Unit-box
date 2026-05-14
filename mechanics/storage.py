import random
from .base import GameObject


class StorageContainer(GameObject):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.slots = int(self.config.get("slots", 8))
        self.items: dict[str, int] = {}
        self.fill_random()

    def fill_random(self) -> None:
        for entry in self.config.get("possible_items", []):
            if random.random() <= float(entry.get("chance", 0.5)):
                self.items[entry["id"]] = random.randint(int(entry.get("min_qty", 1)), int(entry.get("max_qty", 1)))
