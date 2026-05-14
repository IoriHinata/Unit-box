from __future__ import annotations
import importlib
import json
from dataclasses import dataclass, field
from pathlib import Path

from mechanics.player import Player


@dataclass
class World:
    objects: list = field(default_factory=list)
    player: Player | None = None


def load_object_config(obj_type: str) -> dict:
    path = Path("objects") / f"{obj_type}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"type": obj_type, "name": obj_type, "height": 1, "width": 1, "collision": False}


def class_name_from_type(obj_type: str) -> str:
    return "".join(part.capitalize() for part in obj_type.split("_"))


def create_object(obj_type: str, col: int, row: int):
    cfg = load_object_config(obj_type)
    module = importlib.import_module(f"mechanics.{obj_type}")
    cls = getattr(module, class_name_from_type(obj_type), None)
    if cls is None:
        from mechanics.base import GameObject
        cls = GameObject
    return cls(col, row, cfg)


def load_world(config_path: str = "world_config.json") -> World:
    world = World()
    player_cfg = load_object_config("player")
    world.player = Player(1, 1, player_cfg)
    world.objects.append(world.player)
    path = Path(config_path)
    if not path.exists():
        return world
    data = json.loads(path.read_text(encoding="utf-8"))
    for obj in data.get("objects", []):
        world.objects.append(create_object(obj["type"], obj.get("col", 0), obj.get("row", 0)))
    return world


def game_loop(turns: int = 50):
    world = load_world()
    for _ in range(turns):
        for obj in world.objects:
            obj.update(world)
    print("Game finished", {"player_hp": world.player.hp, "objects": len(world.objects)})


if __name__ == "__main__":
    game_loop()
