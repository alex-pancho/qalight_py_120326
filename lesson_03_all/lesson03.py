user_age = 18 # int
user_name = "Stepan" # str
is_student = True # bool

USER_AGE = 19

"""
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
"""

"""
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
"""
імя = "текст"
print(імя)


a = 5
b = 2
result = a + b
print(result)


a = 5
b = 2
result = a / b
print(result)

a = 5
b = 2
result = a // b
print(result)

a = 5
b = 2
result = a % b
print(result)


a = 2
b = 8
result = a ** b
print(result)

a = True
b = False
result = a and b

a = True
b = False
result = a or b

a = True
b = not a

"""
(       )       [       ]       {       }
,       :       .       ;       @
"""

result = (2 + 3) * 4
print(result)

my_list = [1, 2, 3, 4]
print(my_list[2])

my_dict =  {'ключ': 'значення', "key2": 'value2'}
print(my_dict["key2"])

my_set = {1, 2, 3}
my_tuple = (0, "asd", 3)

"""
if умова:
    # Блок коду
    дії()

def функція():
    # Блок коду
    return

"""
ms_str = "Привіт"
my_len = ms_str.__len__()
print(my_len)
print(len(ms_str))

value_1 = 1; value_2 = 1 + 2

"""
@декоратор
def функція():
    # Блок коду
    return
"""
single_quotes = 'Це рядок з одинарними лапкми'
double_quotes = "Це рядок з звичайними, подвійими лапкми"
long_quotes = '''Це \
рядок з тикратним \
повторенням лапок'''
long_quotes_2 = " ggghghh \
    dsdfdsf"

print(long_quotes)
print(long_quotes_2)


ціле_число = 42
восьмеричне_число = 0o52
шістнадцяткове_число = 0x2A
двійкове_число = 0b101010

"""
32-бітних системах це може бути від -2,147,483,648 до 2,147,483,647,
 а на 64-бітних системах це може бути від -9,223,372,036,854,775,808 до 9,223,372,036,854,775,807
"""

num_1 = 10.25
num_2 = 1.2555

число_з_плаваючою_точкою = 3.14
число_з_науковою_нотацією = 2.0e-3
print(число_з_науковою_нотацією)

a = 0.1 + 0.2
b = 0.3

print("a =", repr(a))
print("b =", repr(b))
print("a == b:", a == b)
print("Різниця (a - b):", a - b)

True == 1 #, 2, 3
False == 0
None

'I\'m a Python fanatic'  # You can escape a quote
"I'm a Python fanatic"  # This way may be more readable
'A not very long string' \
'that spans two lines' # Comment not allowed on previous line
# triple-quoted string literal
"""An even bigger
string that spans
three lines*"""  # Comments not allowed on previous lines

single_quotes = 'Це рядок з одинарними лапкми'
print(single_quotes[0])
print(single_quotes[1])
print(single_quotes[1:4])

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
out = '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
print(out)

query_sting = "підказка, що буде виведена на екран і повинна пояснити,\
  що ми очікуємо від користувача: "
variable = input(query_sting)

print("ви ввели: %s" % variable)