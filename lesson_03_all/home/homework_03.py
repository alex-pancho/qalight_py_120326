"""
Домашнє завдання: Основи Python

**1.** Створіть три змінні з правильними іменами (англійською мовою): 
одну для збереження віку, 
одну для імені студента, 
одну для позначення чи є особа студентом. 
Додайте коментарі до кожної змінної.
"""
age = 40# variable for age
student_name  = "Yevhen" # variable for student name
is_student = True

"""

**2.** Рзкоментуйте та виправте помилки в наступних назвах змінних.
Поясніть у коментарях, чому початкові назви неправильні:
"""
name = "John" # "2name" змінна мість число хоча в умові повинно бути просто назва змінної у вигляді слова 
user_age = 25 # тире означає символ віднімання 
price = 100 # символ $ не дозволений у назвах змінних 
subject = "Math" # "class" є зарезерввованим словом у Python і викличе помилку при виконанні цього коду
"""
**3.** Створіть змінну з описовим ім'ям для збереження максимальної кількості студентів у групі. 
Присвойте їй значення 30.
"""
max_student_in_group = 30

"""
**4.** Створіть змінні для збереження: 
назви курсу, 
кількості годин, 
вартості курсу. 
Використайте правильне іменування змінних.
"""
course_name = "QАLight AUT Python G16"
course_hours = 48

"""
**5.** Розрахуйте та виведіть Затрати курсу: 
Затрати курсу  = кількість годин / вартість курсу
Використайте правильне іменування змінних.
"""
course_hourse = 48
course_price = 15840
course_cost = course_hourse / course_price
print("Затрати курсу:", course_cost)

"""
**6.** Створіть змінні з різними способами запису чисел:
- Десяткове число: 42
- Двійкове число: 101010 (в двійковій системі)
- Шістнадцяткове число: 2A (в шістнадцятковій системі)
- Восьмеричне число: 52 (в восьмеричній системі)
"""
decimal_number = 42.5
binary_number = 0b101010
hex_number = 0x2A
octal_number = 0o52

"""
**7.** Виконайте всі арифметичні операції (+, -, *, /, //, %, **) з числами 17 та 5. 
Виведіть результати з поясненнями.
"""
add = 17 + 5
subtraction = 17 - 5
multiplication = 17 * 5
division = 17 / 5
floor_division = 17 // 5
remainder = 17 % 5
exponent = 17 ** 5
print(add)
print(subtraction)
print(multiplication)
print(division)
print(floor_division)
print(remainder)
print(exponent)

"""
**8.** Обчисліть площу кола з радіусом 7.5. Використайте значення π = 3.14159.
"""
π = 3.14159
circle_radius = 7.5
circle_area = π * (circle_radius * circle_radius)
print(round(circle_area, 2))

"""
**9.** Обчисліть залишок від ділення будь-якого числа на 7. 
Виведіть результат з числами 50, 33, 14.
"""

division_1 = 50 % 7
division_2 = 33 % 7
division_3 = 14 % 7
print(division_1)
print(division_2)
print(division_3)

"""
**10.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_see_square = 436402
azov_see_square = 37800
total_see_square = black_see_square + azov_see_square
print(total_see_square)

"""
**11.** Створіть рядок з вашим повним ім'ям та виведіть:
- Перший символ
- Останній символ  
- Довжину рядка
"""
my_name = "Yevhen"
first_latter = my_name[0]
last_latter = my_name[-1]
length = len(my_name)
print(first_latter)
print(last_latter)
print(length)

"""
**12.** Створіть рядок "Would you tell me, please, which way I ought to go from here?" 
та отримайте з нього підстрічки:
- Перші 6 символів
- Останні 11 символів
"""
sentence = "Would you tell me, please, which way I ought to go from here?"
first_six_symbols = sentence[:6]
last_eleven_symbols = sentence[-11:]
print(first_six_symbols)
print(last_eleven_symbols)

"""
**13.** Створіть багаторядковий рядок (використовуючи потрійні лапки) зі своїм улюбленим віршем або цитатою.
"""
favourite_poem = """
The fear of the Lord 
is the beginning of wisdom 
(Bible, Proverbs, 1:7)
"""
print(favourite_poem)

"""
**14.** Поєднайте два рядки "Hello" та "World" у різні способи (з пробілом, з комою, з новим рядком).
"""
word_1 = "Hello"
word_2 = "World"
combined_with_space = word_1 + " " + word_2
combined_with_comma = word_1 + ", " + word_2
combined_with_new_line = word_1 + "\n" + word_2
print(combined_with_space)
print(combined_with_comma)
print(combined_with_new_line)

"""
**15.** Створіть рядок з символами, які потребують екранування (лапки, зворотна коса риска).
"""
example_1 = "Євген вирішив: \"Я вивчу автоматизацію тестування!\""
example_2 = "Цей приклад показує як виглядає знак зворотної косої риски: \\"
print(example_1)
print(example_2)

"""
**16.** Напишіть код, який запитує у користувача його ім'я та вік, 
а потім виводить привітання у форматі: "Привіт, [ім'я]! Тобі [вік] років."
"""
user_name = "Yevhen"
user_age = 37
print(f"Привіт, {user_name}! Tобі {user_age} років")

"""

**17.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8
total_pages = total_photos / photos_per_page
print(int(total_pages))

"""
**18.** Напишіть код який запитує у користувача 
його улюблений колір та число, а потім створює персоналізоване
повідомлення використовуючи f-string форматування.
"""
favourite_colour = "чорний"
favourite_number = 23
message = f"улюблений колір Євгена — {favourite_colour}, " \
          f"улюблене число Євгена — {favourite_number}."
print(message)

"""
**19.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_stuff = 375291
first_and_second = 250449
second_and_third = 222950
warehouse_1 = total_stuff - first_and_second
warehouse_2 = second_and_third - warehouse_1
warehouse_3 = first_and_second - warehouse_2
print("first warehouse:", warehouse_3, "stuff")
print("second warehouse:", warehouse_2, "stuff")
print("third warehouse:", warehouse_1, "stuff")

"""
**20.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_payment = 1179
one_year_and_a_half = 18
total_computer_price = 1179 * 18
print("Загальна вартість комп’ютера:", total_computer_price, "грн")