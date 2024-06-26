import random
import pathlib

current_dir = pathlib.Path(__file__).parent

def get_random_joke():
    """
    Ця функція читає файл з анекдотами та повертає випадковий анекдот.

    Якщо файл з анекдотами не знайдено, функція повертає повідомлення про помилку.

    Returns:
        str: Випадковий рядок з файлу jokes.txt або повідомлення про помилку.
    """

    try:
        with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."