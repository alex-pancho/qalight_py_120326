import re

text = """
Телефонний номер: 123-456-7890
dfklsfjsfjasdlk jdasflkjdasklf jdsfkl djf lkd\
sdkfaj dsk 044-455-2205 
044-455-22-05 
044 455-22-05 
044455-22-05
(123) 456-7890
"""

pattern = r'\(\d{3}\) \d{3}-\d{4}'
    
match = re.search(pattern, text)
if match:
    phone_number = match.group()
    print("Найдено номер телефону:", phone_number)


pattern2 = r'\d{3}(-|\s)?\d{3}-(\d{4}|\d{2}-\d{2})'
    
match = re.findall(pattern2, text)
if match:
    for m in match:
        phone_number = m
        print("Найдено номер телефону:", phone_number)


email = "user@example.com"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
