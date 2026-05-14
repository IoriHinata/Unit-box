from __future__ import annotations
from .base import GameObject


class Player(GameObject):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.speed = float(self.config.get("speed", 1.0))
        self.hp = int(self.config.get("hp", 100))
        self.food = int(self.config.get("food", 100))
        self.inventory: dict[str, int] = {}
        self.target: tuple[int, int] | None = None

    def set_target(self, col: int, row: int) -> None:
        self.target = (col, row)

    def move_step(self) -> None:
        if not self.target:
            return
        tc, tr = self.target
        if self.col < tc:
            self.col += 1
        elif self.col > tc:
            self.col -= 1
        if self.row < tr:
            self.row += 1
        elif self.row > tr:
            self.row -= 1
        if (self.col, self.row) == self.target:
            self.target = None

    def update(self, world: any) -> None:
        self.move_step()
