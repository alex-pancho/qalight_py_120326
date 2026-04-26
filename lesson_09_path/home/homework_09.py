### Робота з файлами та папками — завдання
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
from pathlib import Path

file_path = Path("lesson_09_path/home/hello.txt")
file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.write_text("Hello, Python!", encoding="utf8")

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
with Path("lesson_09_path/home/hello.txt").open(encoding="utf8") as my_file:
    content = my_file.read()
    print(content)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
with Path("lesson_09_path/home/hello.txt").open("a", encoding="utf8") as my_file:
    my_file.write("\nLearning file operations.")

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
with Path("lesson_09_path/home/hello.txt").open("r", encoding="utf8") as my_file:
    for line in my_file:
        print(line.strip())

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
with Path("lesson_09_path/home/hello.txt").open("r", encoding="utf8") as my_file:
        content = my_file.read()
print("Загальна кількість символів у `hello.txt` файлі:", len(content))

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
file_path = Path("lesson_09_path/data/notes.txt")
file_path.parent.mkdir(parents=True, exist_ok=True)

with file_path.open("w", encoding="utf8") as my_file:
    my_file.write("My first note.")

with file_path.open("r", encoding="utf8") as my_file:
    print(my_file.read())

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
folder = Path("lesson_09_path/data")

for file in folder.iterdir():
    if file.is_file():
        print(file.name)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
data_folder = Path("lesson_09_path/data")

file1 = data_folder / "notes.txt"
file2 = data_folder / "copy.txt"

with file1.open("r", encoding="utf8") as my_file:
     content = my_file.read()
with file2.open("w", encoding="utf8") as my_file:
   my_file.write(content)

print("Контент скопійовано успішно!")

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
data_folder = Path("lesson_09_path/data")

file_a = data_folder / "a.txt"
file_b = data_folder / "b.txt"
file_c = data_folder / "ab.txt"

with file_a.open("w", encoding="utf8") as my_file:
   my_file.write("My random text 1")
with file_b.open("w", encoding="utf8") as my_file:
   my_file.write("My random text 2")
with file_a.open("r", encoding="utf8") as my_file:
   content_a = my_file.read()
with file_b.open("r", encoding="utf8") as my_file:
   content_b = my_file.read()
with file_c.open("w", encoding="utf8") as my_file:
   my_file.write(content_a + "\n" + content_b)

print("Контент з 'a.txt' та 'b.txt' файлів успішно скопійовано до 'ab.txt' файлу")

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
file_path = Path("lesson_09_path/data/notes.txt")

with file_path.open("r", encoding="utf8") as my_file:
   file_words = my_file.read()

   if "note" in file_words:
    print("Знайдено")
   else:
    print("Не знайдено")