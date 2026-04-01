
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

