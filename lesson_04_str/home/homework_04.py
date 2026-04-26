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

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
word_list = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(word_list)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_char_h = adwentures_of_tom_sawer.count("h")
print(f"Кількість літер 'h': {count_char_h}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
upper_char_count = 0
for i in range(len(adwentures_of_tom_sawer)):
    adwentures_of_tom_sawer_tmp = adwentures_of_tom_sawer[i]
    if adwentures_of_tom_sawer_tmp.isupper():
        upper_char_count +=1
print (upper_char_count)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom = adwentures_of_tom_sawer.find("Tom")
second_tom = adwentures_of_tom_sawer.find("Tom", first_tom + 1)
print("Другий Том стоїть на позиції:", second_tom)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentence_4 = adwentures_of_tom_sawer_sentences[3]
print("Четверте речення маленькими буквами:", sentence_4.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
by_the_time_check = "By the time" in adwentures_of_tom_sawer_sentences[3]
print("Чи починається речення з 'By the time':", by_the_time_check)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last = adwentures_of_tom_sawer_sentences[-1]
words_in_last = len(last.split())
print("Слів в останньому реченні:", words_in_last)