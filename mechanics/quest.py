import json
from pathlib import Path


class QuestManager:
    def __init__(self, quests_dir: str = "quests"):
        self.quests_dir = Path(quests_dir)
        self.quests = {}
        self.active_quest = None
        self.progress = {}
        self.load()

    def load(self):
        self.quests = {}
        if not self.quests_dir.exists():
            return
        for path in self.quests_dir.glob("*.json"):
            data = json.loads(path.read_text(encoding="utf-8"))
            self.quests[data["id"]] = data

    def start(self, quest_id: str) -> bool:
        if quest_id not in self.quests:
            return False
        self.active_quest = quest_id
        self.progress = {"step": 0}
        return True
