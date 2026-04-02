# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]

small_list = set(small_list)
print(small_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
avg = sum((small_list)) // len((small_list))
print("Середнє арифметичне всіх елементів у списку 'small_list':", avg)

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
if len(big_list) != len(set(big_list)):
    print("Дублікати присутні")
else:
    print("Дублікати відсутні")

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
key = max(add_dict, key=add_dict.get)
print("Ключ з максимальним значенням у словнику 'add_dict':", key)

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
new_dict = {value: key for key, value in base_dict.items()}
print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
for key in set(base_dict) | set(add_dict):
    if key in base_dict and key in add_dict:
        sum_dict[key] = str(base_dict[key]) + str(add_dict[key])
    elif key in base_dict:
        sum_dict[key] = base_dict[key]
    else:
        sum_dict[key] = add_dict[key]

print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
new_set_line = set(line)
print(new_set_line)


# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_unique_set = sum(set_1 ^ set_2)
print("Сума елементів двох множин, які не є спільними складає:", sum_unique_set)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32), ('David', 28), ('Emma', 22), ('Frank', 45)]

list_1 = person_list[:4]
list_2 = person_list[2:]

result = set(list_1) ^ set(list_2)

print(result)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
result = {}

for name, age in person_list:
    lower = (age // 10) * 10
    upper = lower + 9
    key = f"{lower}-{upper}"
    initial = name
    
    if key not in result:
        result[key] = []
    result[key].append(initial)

sorted_result = dict(sorted(result.items(), key=lambda x: int(x[0].split('-')[0])))

print(sorted_result)