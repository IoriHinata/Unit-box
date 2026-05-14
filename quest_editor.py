import json
from pathlib import Path


def create_quest(path: str, quest: dict) -> None:
    Path(path).write_text(json.dumps(quest, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    sample = {
        "id": "q_intro",
        "name": "Первый шаг",
        "description": "Соберите 3 палки",
        "initiator": {"type": "npc_neutral", "col": 2, "row": 2},
        "steps": [{"npc_text": "Помоги мне", "objective": "collect:stick:3", "reward": {"xp": 10}}],
        "next_quest": None,
    }
    create_quest("quests/q_intro.json", sample)
    print("Quest created")
