from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding="UTF_8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
new_list = []
name = []
# firstname =[]
# surname = []
phones = []
email = []

for q in contacts_list:
    for w in q:
        # print(w)
        fio = r'([А-Я]{1}[а-яё]{1,23})\s([А-Я]{1}[а-яё]{1,23})\s?([А-Я]{1}[а-яё]{1,23})?'
        compiled1 = re.compile(fio)
        result = re.search(fio, str(w))
        # print(result)
        if result != None:
            name.append(result)

        phone = r'(\+\d|\d)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})(\s\(?доб.\s\d+)?'
        # sub = r'+7(\3)\4-\5-\6\s\7'
        compiled2 = re.compile(phone)
        result2 = compiled2.match(str(w))
        # sub_result = re.sub(phone, sub, w) ПРИ ЗАМЕНЕ ВЫДАЁТ ГОРУ ОШИБОК, ПРОБЛЕМА В ЦИКЛЕ? Как вывести текст из списка в текст?
        # print(result2)
        if result2 != None:
            phones.append(result2)

new_list.append(contacts_list[0])
p_n = [zip(name, phones)] # Как увидеть в принте ZIP?
print(p_n)
new_list.append(p_n)
print(new_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)
