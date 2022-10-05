from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding="UTF_8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
text = []
lastname = []
firstname =[]
surname = []
organization = []
position = []
phone = []
email = []

for q in contacts_list:
    w = (" ".join(q))
    print(w)
    pattern1 = r'([А-Я]{1}[а-яё]{1,23})\s([А-Я]{1}[а-яё]{1,23})\s?([А-Я]{1}[а-яё]{1,23})?'
    compiled1 = re.compile(pattern1)
    result = re.findall(pattern1, str(q))
    print(result)

    pattern2 = r'(\+7|8)?\s?\(?(\d+)\)?\s?(\d+)[-|\s]?(\d+)[-|\s]?(\d+)\(?[доб.]?\s?(\d+)?'
    compiled2 = re.compile(pattern2)
    result2 = compiled2.findall(str(q))
    print(result2)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
