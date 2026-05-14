import random
from .base import GameObject


class NeutralNPC(GameObject):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.zone_radius = int(self.config.get("zone_radius", 3))
        self.home = (self.col, self.row)

    def update(self, world: any) -> None:
        if random.random() < 0.1:
            self.col += random.choice([-1, 0, 1])
            self.row += random.choice([-1, 0, 1])
            hc, hr = self.home
            self.col = max(hc - self.zone_radius, min(hc + self.zone_radius, self.col))
            self.row = max(hr - self.zone_radius, min(hr + self.zone_radius, self.row))
