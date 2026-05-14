from .npc_enemy import EnemyNPC


class AllyNPC(EnemyNPC):
    def update(self, world: any) -> None:
        enemies = [o for o in world.objects if o.type == "npc_enemy"]
        if not enemies:
            return
        target = min(enemies, key=lambda e: abs(e.col - self.col) + abs(e.row - self.row))
        if target.col > self.col:
            self.col += 1
        elif target.col < self.col:
            self.col -= 1
        if target.row > self.row:
            self.row += 1
        elif target.row < self.row:
            self.row -= 1
