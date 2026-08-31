adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

correct_text_1 = adwentures_of_tom_sawer.replace("\n"," ")
print("Завдання 1")
print(correct_text_1)

# task 02 ==
""" Замініть .... на пробіл """

correct_text_2= correct_text_1.replace("...."," ")

print("Завдання 2")
print(correct_text_2)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

correct_text_3 = correct_text_2.replace("  "," ")

print("Завдання 3")
print(correct_text_3)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h" 
"""
count_h = correct_text_3.count("h")

print("Завдання 4")
print("Кількість літер 'h' в тексті:" , count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""

upper_letters = sum(1 for symbol in adwentures_of_tom_sawer if symbol.isupper())

print("Завдання 5")
print("Кількість великих літер в тексті:", upper_letters)
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

word = "Tom"
first_time_Tom = adwentures_of_tom_sawer.find(word)
second_time_Tom = adwentures_of_tom_sawer.find(word, first_time_Tom, +1)


print("Завдання 6")
print("Позиція, на якій слово 'Tom' зустрічається вдруге:" , second_time_Tom)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = correct_text_3.split(".")

print("Завдання 7")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print("Завдання 8")
if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("Завдання 9")
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print("Так, є речення, яке починається з 'By the time'.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("Завдання 10")
words_in_story = adwentures_of_tom_sawer.split()
last_tree_words = words_in_story[-3:]
result = " ".join(last_tree_words)
print("Останні три слова тексту:", result)