import random
from .base import GameObject


class ResourceNode(GameObject):
    def harvest(self, tool: str | None = None) -> list[tuple[str, int]]:
        required = self.config.get("tool_required")
        if required and tool != required:
            return []
        result = []
        for entry in self.config.get("loot_table", []):
            if random.random() <= float(entry.get("chance", 1.0)):
                qty = random.randint(int(entry.get("min_qty", 1)), int(entry.get("max_qty", 1)))
                result.append((entry["id"], qty))
        return result
