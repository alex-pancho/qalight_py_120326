from pathlib import Path

### Робота з файлами та папками — завдання
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
with open('lesson_09_path/home/hello.txt', 'w', encoding='utf-8') as f:
   f.write('Hello, Python!')

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
with open('lesson_09_path/home/hello.txt', 'r') as f:
    content = f.read()
    print(content)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
with open('lesson_09_path/home/hello.txt', 'a') as f:
    f.write('\n Learning file operations.')

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
with open('lesson_09_path/home/hello.txt', 'r', encoding='utf-8') as f:
   for line in f:
      print(line.rstrip())

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
with open('lesson_09_path/home/hello.txt', 'r', encoding='utf-8') as f:
   text = f.read()
   ch_sum = len(text)
   print(ch_sum)

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
path_to_dir = Path('lesson_09_path/home/data')
path_to_dir.mkdir(exist_ok=True)
path_to_file = path_to_dir/"notes.txt"
with open(path_to_file, 'w', encoding="utf-8") as f:
   f.write('My first note.')

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
for item in path_to_dir.iterdir():
    print(item)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
content_from_notes = None
path_to_new_file = path_to_dir/"copy.txt"
with open(path_to_file, 'r') as f:
   content_from_notes = f.read()
with open(path_to_new_file, 'w' ,encoding='utf-8') as f:
   f.write(content_from_notes)

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
with open(path_to_dir/'a.txt', 'w', encoding='utf-8') as f:
    f.write('AAAAAAAAAAAAAAA')

with open(path_to_dir/'b.txt', 'w', encoding='utf-8') as f:
    f.write('BBBBBBBBBBBBBBBB')

with open(path_to_dir/'ab.txt', 'w', encoding='utf-8') as result_file:
    with open(path_to_dir / 'a.txt', 'r', encoding='utf-8') as f_a:
        text_a = f_a.read()
        result_file.write(text_a)
    with open(path_to_dir / 'b.txt', 'r', encoding='utf-8') as f_b:
        text_b = f_b.read()
        result_file.write(text_b)

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
with open(path_to_file, 'r', encoding='utf-8') as f:
    content = f.read()
    if "note" in content.lower():
        print("Знайдено")
    else:
        print("Не знайдено")