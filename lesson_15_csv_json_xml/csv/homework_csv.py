import csv
from pathlib import Path

def read_file(filepath: Path) -> list:
    """Читає CSV файл і повертає список списків (рядків)."""
    if not filepath.exists():
        print(f"Файл {filepath.name} не знайдено.")
        return []
    
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def write_csv(filepath: Path, content: list):
    """Записує список списків у CSV файл."""
    if not content:
        return
    
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(content)

def get_unique_rows(file_paths: list) -> list:
    """Об'єднує файли та повертає лише унікальні рядки, зберігаючи заголовок."""
    unique_data = []
    seen = set()
    header = None

    for path in file_paths:
        rows = read_file(path)
        if not rows:
            continue
        
    
        if header is None:
            header = rows[0]
            unique_data.append(header)
        
       
        for row in rows[1:]:
           
            row_tuple = tuple(row)
            if row_tuple not in seen:
                unique_data.append(row)
                seen.add(row_tuple)
                
    return unique_data

if __name__ == "__main__":
    base_path = Path(__file__).parent
    
   
    file1 = base_path / "users_1.csv"
    file2 = base_path / "users_2.csv"
    output_file = base_path / "clean_users_3.csv"
    
    
    cleaned_content = get_unique_rows([file1, file2])
 
    write_csv(output_file, cleaned_content)
    print(f"Очищено рядків: {len(cleaned_content)}. Результат у {output_file.name}")