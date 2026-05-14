import json
from pathlib import Path


def ensure(path: Path, default):
    if not path.exists():
        path.write_text(json.dumps(default, ensure_ascii=False, indent=2), encoding="utf-8")


def init_files():
    ensure(Path("recipes.json"), [])
    ensure(Path("world_config.json"), {"structures": [], "objects": []})


def main():
    init_files()
    print("Map editor skeleton ready.")


if __name__ == "__main__":
    main()
