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
    # print(q)
    pattern1 = r'(\w+)\s(\w+)\s(\w+)|(\w+)|(\w+)\s(\w+)'
    compiled = re.compile(pattern1)
    result = compiled.findall(str(q))
    print(result[0:3])
    # firstname.append(result[0])

# pattern2 = r'(\+7|8)\s?[(\s]?(\d+)[)\s-][\s-]?(\d+)-(\d\d)-?(\d+)\s?(?(доб.)?\s?(\d+)?)?'
# compiled = re.compile(pattern2)
# result1 = compiled.findall(q)
# print(result1)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
