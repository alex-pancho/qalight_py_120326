from lxml import html
import requests

url = "https://qalight.ua/"

response = requests.get(url)
html_content = response.text
tree = html.fromstring(html_content)
# Заголовок
title = tree.xpath('//title/text()')[0]
print("Заголовок сторінки:", title)

# Вилучення тексту з усіх тегів <a> за допомогою XPath
links = tree.xpath('//a/text()')
for link in links:
    print("Посилання:", link)

# Логотипи

xpath_1 = '//div[contains(@class, "logo-block")]'
logos = tree.xpath(xpath_1)
print(f"Знайдено логотипів: {len(logos)}")
# Текст
xpath_2 = '//p[contains(text(), "Курси QALight - це Ваша можливість")]'
paragraphs = tree.xpath(xpath_2)
if paragraphs:
    print("Знайдений текст параграфа:", paragraphs[0].text_content().strip())


# Хедери
xpath_3 = '//h2'
headers_h2 = tree.xpath(xpath_3)
# Виведення результату
if headers_h2:
    print("Текст першого заголовку H2:", headers_h2[0].text_content().strip())
else:
    print("Заголовки H2 не знайдено.")
# Кнопки
xpath_4 = '//a[contains(text(), "Запис")]'
button = tree.xpath(xpath_4)
if button:
    print(f"Успішно знайдено кнопок: {len(button)}")


# Меню хедер
xpath_5 = '//a[contains(text(), "Контакти")]'
menu = tree.xpath(xpath_5)

if menu:
    
    target_button = menu[0]

    button_text = target_button.text_content().strip()
    
    button_url = target_button.get('href')
    
    print(f"Текст на знайденому хедер меню: '{button_text}'")
    print(f"Посилання (атрибут href): {button_url}")

# Пошук
xpath_6 = '//div[contains(@class, "search")]'
search = tree.xpath(xpath_6)
if search:
    print(f"Знайдено елементів пошуку: {len(search)}")
  

xpath_7 = '//*[contains(@class, "heading1")]'
elements = tree.xpath(xpath_7)

if elements:
   
    text = elements[0].text_content().strip()
    print(f"Знайдений текст параграфа: {text}")