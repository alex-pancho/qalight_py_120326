# -*- coding: utf-8 -*-
# Самостійне вивчення - Поглиблені задачі
# Виконайте завдання та збережіть результати у вказаних змінних

print("=== ПОГЛИБЛЕНІ ЗАДАЧІ ===")

# Task 1. Створіть список з парних чисел від 2 до 20
even_numbers = list(range(2,22,2))  # Ваш код тут
print(even_numbers)

# Task 2. Відфільтруйте з списку тільки числа більше 10
numbers_list = [5, 12, 8, 15, 3, 18, 7, 20]
filtered_numbers = [x for x in numbers_list if x>10 ]
print(filtered_numbers)

# Task 3. Створіть список квадратів непарних чисел від 1 до 9
odd_squares = [n**2 for n in range (1,10,2)]
print(odd_squares)


# Task 4. Об'єднайте два списки без дублікатів
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
set1= set(list1)
set2 = set(list2)
merged_unique = set1.union(set2)
print (merged_unique) # Ваш код тут

# Task 5. Створіть кортеж з координатами точок
points = tuple((i,i) for i in range(3))  # Ваш код тут: ((0,0), (1,1), (2,2))
print(points)


# Task 6. Розпакуйте кортеж координат
coordinates = (10, 20, 30)
x, y, z = 10, 20, 30  # Ваш код тут
print (x, y, z)

# Task 7. Створіть множину голосних літер
vowels = {'a', 'e', 'i', 'o', 'u'}

# Task 8. Знайдіть унікальні символи у рядку
text = "programming"
unique_chars = set(text)  # Ваш код тут
print(unique_chars)

# Task 9. Створіть множину чисел, які діляться на 3 від 1 до 15
divisible_by_3 = set((a for a in range(1,16) if a % 3 ==0 ))  # Ваш код тут
print(divisible_by_3)

# Task 10. Знайдіть симетричну різницю двох множин
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)  # Ваш код тут

# Task 11. Створіть словник з кількістю символів у кожному слові
words = ["cat", "dog", "elephant", "bee"]
word_lengths ={word: len(word) for word in words} # Ваш код тут: {"cat": 3, "dog": 3, ...}
print(word_lengths)


# Task 12. Створіть словник з квадратами та кубами чисел
numbers = [2, 3, 4, 5]
powers_dict = {n: {"square": n**2, "cube": n**3} for n in numbers}  # Ваш код тут: {2: {"square": 4, "cube": 8}, ...}
print(powers_dict)

# Task 13. Згрупуйте слова за їх довжиною
word_list = ["apple", "cat", "dog", "banana", "car", "elephant"]
grouped_by_length = {}
for word in word_list:
    length = len(word)
    if length not in grouped_by_length:
        grouped_by_length[length] = []
    grouped_by_length[length].append(word)  # Ваш код тут
print(grouped_by_length)

# Task 14. Створіть словник частоти символів у рядку
sentence = "hello world"
char_frequency = {}  # Ваш код тут
for char in sentence:
    char_frequency[char] = char_frequency.get(char, 0) + 1
print(char_frequency)

# Task 15. Об'єднайте декілька словників
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}
dict1.update(dict2)  # Ваш код тут
#print(dict1)
dict1.update(dict3)
print(dict1)

# Task 16. Інвертуйте словник (ключі стають значеннями)
original = {"name": "John", "age": 25, "city": "Kyiv"}
inverted = {value: key for key, value in original.items()}
print(inverted)  # Ваш код тут

# Task 17. Створіть список кортежів з словника
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
score_tuples = list(scores.items())  # Ваш код тут: [("Alice", 95), ...]
print(score_tuples)

# Task 18. Знайдіть спільні ключі у двох словниках
dict_a = {"x": 1, "y": 2, "z": 3}
dict_b = {"y": 5, "z": 6, "w": 7}
common_keys = dict_a.keys() & dict_b.keys()  # Ваш код тут
print(common_keys)

# Task 19. Створіть вкладений словник з інформацією про студентів
students_info = {
    
    "student1": {"name": "Олена", "grades": [90, 85, 92]},
    "student2": {"name": "Максим", "grades": [78, 88, 80]},
    "student3": {"name": "Андрій", "grades": [95, 92, 98]}
}
 # Ваш код тут: {"student1": {"name": ..., "grades": [...]}, ...}

# Task 20. Сплюсніть всі списки у словнику
data = {"list1": [1, 2], "list2": [3, 4], "list3": [5, 6]}

flattened = [item for sublist in data.values() for item in sublist]
print(flattened)
# Ваш код тут: [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    print("\n=== ЗАВЕРШЕННЯ ===")
    print("Поглиблені завдання виконано! Запустіть test_selflearning.py для перевірки.")