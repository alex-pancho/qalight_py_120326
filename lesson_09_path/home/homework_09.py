### Робота з файлами та папками — завдання
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
from pathlib import Path

current_file = Path(__file__)
current_folder = current_file.parent 
hello_file = current_folder / "hello.txt"

print(hello_file.absolute())

with open(hello_file, 'w') as f:
    f.write('Hello, Python!')
"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
with open('hello.txt', 'r') as f:
    content = f.read()
    print(content)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
with open('hello.txt', 'a') as f:
    f.write('\nLearning file operations.')

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
with open('hello.txt', 'r') as f:
    content = f.read()
    print(content)

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
hello_file = current_folder / "hello.txt"
if hello_file.exists():
    with open(hello_file, 'r', encoding='utf-8') as f:
        content = f.read()
        count = len(content)
        
    print(f"Кількість символів у файлі '{hello_file.name}': {count}")
else:
    print(f"Файл {hello_file.name} не знайдено!")

print(f"Папка файлу: {hello_file.parent.absolute()}")
"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
data_folder = current_file.parent / "data"
data_folder.mkdir(parents=True, exist_ok=True)
data_file = data_folder / "notes.txt"
print(data_file.exists())
with data_file.open("w", encoding="utf8") as f:
    f.write("My first note.") 

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
files = [f for f in data_folder.iterdir() if f.is_file()]
print(files)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
copy_file = data_folder / "copy.txt"
with open(data_file, 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"Вміст файлу: {content}")
with open(copy_file, 'w', encoding='utf-8') as f:
    f.write(content)
    

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
path_a = data_folder / "a.txt"
path_b = data_folder / "b.txt"
path_ab = data_folder / "ab.txt"
with open(path_a, 'w', encoding='utf-8') as f:
    f.write("Test file A")
with open(path_b, 'w', encoding='utf-8') as f:
    f.write("Test file B")  

with open(path_a, 'r', encoding='utf-8') as f:
    content_a = f.read()


with open(path_b, 'r', encoding='utf-8') as f:
    content_b = f.read()


with open(path_ab, 'w', encoding='utf-8') as f:
    f.write(content_a)
    f.write("\n")  
    f.write(content_b)

print(f"Готово! Вміст файлів об'єднано в {path_ab.name}")

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
hello_file = data_folder / "notes.txt"
if hello_file.exists():
    with open(hello_file, 'r', encoding='utf-8') as f:
        content = f.read()
        find = content.find ("note")
        
    print("Знайдено ")
else:
    print("Не знайдено!")



