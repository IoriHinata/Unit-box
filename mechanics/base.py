from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class GameObject:
    col: int
    row: int
    config: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.type = self.config.get("type", "object")
        self.name = self.config.get("name", self.type)
        self.collision = bool(self.config.get("collision", False))
        self.height = int(self.config.get("height", 1))
        self.width = int(self.config.get("width", 1))

    def update(self, world: Any) -> None:
        pass

    def draw(self, surface: Any, camera: Any) -> None:
        pass
