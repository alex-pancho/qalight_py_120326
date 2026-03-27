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
paragraph = adwentures_of_tom_sawer.replace("\n", " ")
print("Замінити кінець абзацу на пробіл:", paragraph)


# task 02 ==
""" Замініть .... на пробіл
"""
space_sawer = adwentures_of_tom_sawer.replace("....", " ")
print("Замініть .... на пробіл", space_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
text_space = adwentures_of_tom_sawer.split()
clean_text = " ".join(text_space)
print("Не більше одного пробілу:", clean_text)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print("Кількість літери h:", count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
count_char = 0
for char in adwentures_of_tom_sawer:
    if char.isupper():
        count_char += 1
print("Порахувати кожну велику літеру:", count_char)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom_first = adwentures_of_tom_sawer.find("Tom")
tom_second = adwentures_of_tom_sawer.find("Tom", tom_first + 1)
print("Cлово Tom зустрічається вдруге:", tom_second)
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.replace("\n", " ").split(". ")
print(adwentures_of_tom_sawer_sentences)
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print("Четверте речення - нижній регістр:")
print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
starts_with_by_the_time = any(s.strip().startswith("By the time") for s in adwentures_of_tom_sawer_sentences)
print("чи починається якесь речення з 'By the time'", starts_with_by_the_time)
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentences = adwentures_of_tom_sawer_sentences[-1]
words_in_last_sentence = last_sentences.split()
count_last_sentences = len(words_in_last_sentence)
print(count_last_sentences)