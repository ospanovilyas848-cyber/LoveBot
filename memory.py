import json
import random
from pathlib import Path


MEMORY_FILE = Path(__file__).parent / "memory.json"


def load_memory():
    if not MEMORY_FILE.exists():
        return {}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict):
            return data

    except (json.JSONDecodeError, OSError, TypeError):
        pass

    return {}


def save_memory(data):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )
    except (OSError, TypeError):
        pass


def get_unique_text(user_id: int, category: str, texts: list):

    if not texts:
        return "Здесь пока ничего нет ❤️"

    data = load_memory()

    user_key = str(user_id)

    if user_key not in data or not isinstance(data[user_key], dict):
        data[user_key] = {}

    if category not in data[user_key] or not isinstance(
        data[user_key][category], list
    ):
        data[user_key][category] = []

    used = data[user_key][category]

    used = [
        index
        for index in used
        if isinstance(index, int)
        and 0 <= index < len(texts)
    ]

    used = list(dict.fromkeys(used))

    data[user_key][category] = used

    # Все индексы сообщений
    all_indexes = list(range(len(texts)))

    available = [
        index
        for index in all_indexes
        if index not in used
    ]

    if not available:
        used = []
        data[user_key][category] = used
        available = all_indexes.copy()

    if not available:
        return "Здесь пока ничего нет ❤️"

    index = random.choice(available)

    used.append(index)

    data[user_key][category] = used

    save_memory(data)

    return texts[index]