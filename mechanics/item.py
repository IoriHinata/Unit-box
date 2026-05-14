from dataclasses import dataclass


@dataclass
class Item:
    id: str
    qty: int = 1
    durability: int | None = None
    item_type: str = "material"
    damage: int = 0
