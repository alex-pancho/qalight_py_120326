from lxml import html
import requests

url = "https://lxml.de/"

response = requests.get(url)
html_content = response.text

# Аналіз HTML-документу з використанням lxml
tree = html.fromstring(html_content)

title = tree.findtext('.//title')
print("Заголовок сторінки:", title)

xpath = '//h1[@class="title"]/text()'
title = tree.xpath(xpath)[0]
print(f"Заголовок по {xpath}:", title)

links = tree.xpath('//a/text()')
for link in links:
    print("Посилання:", link)