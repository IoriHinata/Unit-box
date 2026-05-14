from .base import GameObject
from .player import Player
from .wall import Wall
from .npc_neutral import NeutralNPC
from .npc_enemy import EnemyNPC
from .npc_ally import AllyNPC
from .resource import ResourceNode
from .storage import StorageContainer

CLASS_REGISTRY = {
    "player": Player,
    "wall": Wall,
    "npc_neutral": NeutralNPC,
    "npc_enemy": EnemyNPC,
    "npc_ally": AllyNPC,
    "resource": ResourceNode,
    "storage": StorageContainer,
}
