
empty_tuple = ()

sinle_item_tuple_int = (42, )
sinle_item_tuple_str = ("a42", )

mixed_tuple = (1, "hello", 3.14, True, "a", "a", "aaa", ("a", "a"))

first_element = mixed_tuple[0]
fifth_element = mixed_tuple[4]
print(fifth_element)

fifth_element_2 = mixed_tuple[-1]
print(fifth_element_2)

count_item = mixed_tuple.count(1)
print(count_item)

count_item_2 = mixed_tuple.count("a")
print("count(a)", count_item_2)

index_item = mixed_tuple.index(3.14)
print(index_item)

# index_item = mixed_tuple.index("aa")
# print(index_item)

print(mixed_tuple[1:3])

mini_tuple = (93, 5, "a")

a, b, c = mini_tuple

print(c)

my_string = "Привіт, світ!"
tuple_from_string = tuple(my_string)

# Виведення кортежу
print(tuple_from_string)

my_list = [1, 2, 3, 'Python', True, (1, 2, 3), [1,0]]
tuple_from_list = tuple(my_list)

# Виведення кортежу
print(tuple_from_list)

print('y' in 'Python')
print(1 in tuple_from_list)
print('y' in tuple_from_list)
print('y' in tuple_from_list[3])

##

my_list = [1, 2, 3, 'Python', True, (1, 2, 3), [1, 0], 123]

first_element = my_list[0]
fifth_element = my_list[4]
print(first_element)
print(fifth_element)
last_el = my_list[-1]
print(last_el)
subset = my_list[2:7:2] # з кроом
subset = my_list[2:7] # без кроку
print(subset)

count_item = my_list.count(2)
print(count_item)

count_item_2 = my_list.count("a")
print("count(a)", count_item_2)

index_item = my_list.index([1, 0])
print(index_item)

# append
my_list.append(23)
print(my_list)

my_list.append("alex")
print(my_list)

my_list.append([1, 2, 3])
print(my_list)

# extend
# my_list.extend(23) # TypeError: 'int' object is not iterable
# print(my_list)

my_list.extend("alex")
print(my_list)

my_list.extend([1, 2, 3])
print(my_list)

my_list.insert(1, 4)
print(my_list)

my_list.insert(0, "V")
print(my_list)

my_list.remove(1)
print(my_list)

element = my_list.pop(1)
print(element)
print(my_list)
a, b, c = my_list[:3]
print(a, b, c)
first, *mid, last = my_list
print(first, mid, last)

*first, mid, last = my_list
print(first, mid, last)

first, mid, *last = my_list
print(first, mid, last)

# for i in my_list:
#     print(i)
print("==================")
unsort_list = [6, 3, 95, 7, 2, 9, 0, 33, 104]
sort_list = sorted(unsort_list)
print(sort_list)
print(unsort_list)

print("==================")
unsort_list.sort()
print(unsort_list)
words = ["яблуко", "апельсин", "банан", "гру", "слива"]
sort_list = sorted(words)
print(sort_list)
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

my_string = "Привіт, світ!"
list_from_string = list(my_string)
print(list_from_string)
lost_split = my_string.split(", ")
print(lost_split)
long_str = "Приклади створення списків в Python з різних джерел даних. "
long_str_split = long_str.split()
print(long_str_split)
print("в" in long_str_split)

my_tuple = (10, 20, 30, 40, 50)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

numbers_a = [x for x in range(11)]
print(numbers_a)

numbers_b = [x + 2 for x in range(11)]
print(numbers_b)

numbers_c = [x * 2 for x in range(11)]
print(numbers_c)

numbers_d = [x * 2 for x in range(11) if x % 2 == 0]
print(numbers_d)

words = ["яблуко", "груша", "апельсин", "abb"]
word_lengths = [len(word) for word in words]
print(word_lengths)

# set
fruits = {"яблуко", "банан", "апельсин"}

fruits.add("лимон")
fruits.add("яблуко")
fruits.add(1)
print(fruits)
fruits.add(("banana", "kivi"))
print(fruits)
# fruits.add(["olena"])
# print(fruits)
element = "лимон" 
if element in fruits:
    print(f"Елемент {element} присутній в множині.")

random_item = fruits.pop()
print(random_item)

if "яблуко" in fruits:
    fruits.remove("яблуко")
    print(fruits)

my_set = {1, 2, 3}
additional_elements = {4, 5, 6}
#my_set.add(additional_elements) 
my_set.update(additional_elements)
print(f"Оновлена множина: {my_set}")

my_list_22 = [2, 2, 3, 4, 2, 5, 5, 6, 2, 1, 2, 1, 4, 7]
unic = list(set(my_list_22))
print(unic)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

logical_union = set1.union(set2)
# або
logical_union = set1 | set2
print(logical_union)

logical_intersection = set1.intersection(set2)
# або
logical_intersection = set1 & set2
print(logical_intersection)

logical_difference = set1.difference(set2)
# або
logical_difference = set1 - set2
print(logical_difference)

logical_difference = set2 - set1
print(logical_difference)

logical_symmetric_difference = set1.symmetric_difference(set2)
# або
logical_symmetric_difference = set1 ^ set2

print(logical_symmetric_difference)

my_ling_new_str = "Приклади створення множини в Python з інших типів даних за допомогою"
set_from_string = set(my_ling_new_str)
print(set_from_string)

# set()
my_dict = {} # empty dict
en_ua = {"hello": "привіт", "good": "добре", "day": "день", "nice": "приємно", "you": "ти"}

means_1 = en_ua["good"]
print("good", means_1)
# str tuple bool frozenset
# int float None

lat_ua = dict(labore="любов", zelo="знання", calcule="рахувати")
print(lat_ua)

with_tuple_dict =  {(1, 2, 3):'значення1', 10:'значення2' }
print(with_tuple_dict[(1, 2, 3)])


used_params = {'name': 'Василь', 'age': 25, 'city': 'Київ'} #, "job":"IT spec"
user_age = used_params["age"]
print("user age", user_age)
# print(used_params["job"]) # KeyError
print("job" in used_params)
print("get age key", used_params.get("age"))
print("get job key", used_params.get("job"))
print("get job key", used_params.get("job", "Worker"))

all_keys = used_params.keys()
print(all_keys)
all_vals = used_params.values()
print(all_vals)
all_pairs = used_params.items()
print(all_pairs)

for i in used_params:
    print(i)

for i in used_params.keys():
    print(i)

for i in used_params:
    print(i, used_params[i])

for v in used_params.values():
    print(v)

for k, v in used_params.items():
    print(k, v)

sec_dict = {"k1":"v1", "k2":"v2"}
new_dict = sec_dict.copy()
print("sec_dict before", sec_dict)
sec_dict.update({"k3": 123})
print("new_dict", new_dict)
print("sec_dict after", sec_dict)
vals_2 = new_dict.pop('k2', 'значення за замовчуванням')
print(vals_2)

# add value
sec_dict.update({"1": 1})
print(sec_dict)
sec_dict["k99"] = 99
print(sec_dict)

# del
del sec_dict["k99"]
print("del k99", sec_dict)

list_tuple = [('ключ1', 'значення1'), ('ключ2', 'значення2'), ('ключ3', 'значення3')]
dict_from_tuple = dict(list_tuple)
print(dict_from_tuple)

list_lists = [['ключ1', 'значення1'], ['ключ2', 'значення2']]
dict_from_lists = dict(list_lists)
print(dict_from_lists)
some_keys = ('ключA', 'ключB', 'ключC', "a")
some_vals = ("valA", "valB", "valC", "ssd")
dict_from_pairs = dict(zip(some_keys, some_vals))
print(dict_from_pairs)


name_1 = "Олександр"
name_2 = "Alex"

ukrainian_letters = set("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'")
name_set = set(name_1.lower())
diff = name_set - ukrainian_letters
print(diff)

name_set = set(name_2.lower())
diff = name_set - ukrainian_letters
print(diff)
