# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]

unique = list(set(small_list))
print(unique)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
summ = 0
for i in small_list:
    summ += i
average = summ / len(small_list)
print(average)

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

for i in range(len(big_list)):
    tmp = big_list[i]
    for x in big_list[i + 1:]:
        if x == tmp:
            print("Так, дублікати є в біг ліст")
            break
    else:
        continue
    break

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

max_value = max(add_dict, key=lambda k: add_dict[k])
print(max_value)



# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})

new_dict = {}
for key in base_dict:
    value = base_dict[key]
    new_dict[value] = key
print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
def union_dict():
    sum_dict = {}
    for i in base_dict:
        if i in add_dict:
            sum_dict[i] = str(base_dict[i]) + str(add_dict[i])
        else:
            sum_dict[i] = base_dict[i]
    for i in add_dict:
        if i not in sum_dict:
            sum_dict[i] = add_dict[i]
    print(sum_dict)
#union_dict()

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
convert_to_set = set(line)
print(convert_to_set)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
set_sum = 0
connected_set = set_1 | set_2
for i in connected_set:
    set_sum+=i
print(set_sum)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_1_1 = [1, 2, 3, 4]
list_2_2 = [3, 4, 5, 6]

connected_set_new = set(list_1_1).symmetric_difference(set(list_2_2))
print(connected_set_new)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
def task_10():
    person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
    new_dict = {}

    for i in person_list:
        if 10 <= i[1] <= 19:
            if '10-19' not in new_dict:
                new_dict['10-19'] = []
            new_dict['10-19'].append(i[0])

        if 20 <= i[1] <= 29:
            if '20-29' not in new_dict:
                new_dict['20-29'] = []
            new_dict['20-29'].append(i[0])

        if 30 <= i[1] <= 39:
            if '30-39' not in new_dict:
                new_dict['30-39'] = []
            new_dict['30-39'].append(i[0])

        if 40 <= i[1] <= 49:
            if '40-49' not in new_dict:
                new_dict['40-49'] = []
            new_dict['40-49'].append(i[0])
    sorted_dict = dict(sorted(new_dict.items()))
    print(sorted_dict)

task_10()