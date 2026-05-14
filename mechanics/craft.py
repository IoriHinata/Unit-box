import json
from pathlib import Path


class CraftSystem:
    def __init__(self, recipe_path: str = "recipes.json"):
        self.recipe_path = Path(recipe_path)
        self.recipes = self.load_recipes()

    def load_recipes(self):
        if not self.recipe_path.exists():
            return []
        return json.loads(self.recipe_path.read_text(encoding="utf-8"))

    def craft(self, inventory: dict[str, int], recipe_name: str) -> bool:
        rec = next((r for r in self.recipes if r["name"] == recipe_name), None)
        if not rec:
            return False
        for item, qty in rec["ingredients"].items():
            if inventory.get(item, 0) < qty:
                return False
        for item, qty in rec["ingredients"].items():
            inventory[item] -= qty
        res = rec["result"]
        inventory[res["id"]] = inventory.get(res["id"], 0) + int(res.get("qty", 1))
        return True
