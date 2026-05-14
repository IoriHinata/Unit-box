from .base import GameObject


class Wall(GameObject):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.collision = True
