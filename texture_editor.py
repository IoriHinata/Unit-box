import json
from pathlib import Path

TILE_WIDTH = 64
TILE_HEIGHT = 32


def canvas_size(object_json_path: str) -> tuple[int, int]:
    data = json.loads(Path(object_json_path).read_text(encoding="utf-8"))
    width = int(data.get("width", 1))
    height = int(data.get("height", 1))
    return TILE_WIDTH * width, TILE_HEIGHT * height + TILE_HEIGHT


if __name__ == "__main__":
    print("Texture editor helper")
