import json
from pathlib import Path


def read_json(filepath: Path):
    """
    Читає JSON файл та повертає його вміст як Python об'єкт.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        print(f"Помилка: Файл {filepath.name} не знайдено.")
        return None
    except json.JSONDecodeError as e:
        print(f"Помилка валідації у файлі {filepath.name}: {e.msg}")
        return None


def write_json(filepath: Path, content: dict) -> bool:
    """
    Записує Python об'єкт у JSON файл.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(content, file, indent=4, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"Помилка при записі у файл {filepath.name}: {e}")
        return False


if __name__ == "__main__":
    
    base_path = Path(__file__).parent

   
    files_to_check = ["file_01.json", "file_02.json", "file_03.json"]

    print("--- Результати валідації ---")
    
    for filename in files_to_check:
        file_path = base_path / filename
        
       
        if not file_path.exists():
            print(f"Файл {filename} відсутній у директорії.")
            continue

        content = read_json(file_path)
        
        if content is not None:
            print(f" Файл {filename} коректний.")
            