import subprocess

APPS = {
    "1": ("Игра", "game.py"),
    "2": ("Редактор карт", "editor.py"),
    "3": ("Редактор текстур", "texture_editor.py"),
    "4": ("Редактор квестов", "quest_editor.py"),
    "5": ("Редактор модов", "mod_editor.py"),
}


def main():
    print("=== Unit box: Главное меню ===")
    for key, (name, _) in APPS.items():
        print(f"{key}. {name}")
    choice = input("Выберите пункт: ").strip()
    if choice in APPS:
        subprocess.run(["python", APPS[choice][1]], check=False)


if __name__ == "__main__":
    main()
