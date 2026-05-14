from .npc_neutral import NeutralNPC


class EnemyNPC(NeutralNPC):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.damage = int(self.config.get("damage", 5))
        self.hp = int(self.config.get("hp", 20))

    def update(self, world: any) -> None:
        player = world.player
        if abs(player.col - self.col) + abs(player.row - self.row) <= self.zone_radius:
            if player.col > self.col:
                self.col += 1
            elif player.col < self.col:
                self.col -= 1
            if player.row > self.row:
                self.row += 1
            elif player.row < self.row:
                self.row -= 1
            if (self.col, self.row) == (player.col, player.row):
                player.hp = max(0, player.hp - self.damage)
        else:
            super().update(world)
