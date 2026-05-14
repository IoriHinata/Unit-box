from pathlib import Path

TEMPLATE = '''from mechanics.base import GameObject


class {class_name}(GameObject):
    def update(self, world):
        # TODO: generated behavior
        pass
'''


def snake_to_pascal(name: str) -> str:
    return "".join(p.capitalize() for p in name.split("_"))


def generate_mod(name: str) -> Path:
    class_name = snake_to_pascal(name)
    path = Path("mechanics") / f"{name}.py"
    path.write_text(TEMPLATE.format(class_name=class_name), encoding="utf-8")
    return path


if __name__ == "__main__":
    p = generate_mod("custom_boss")
    print(f"Generated: {p}")
