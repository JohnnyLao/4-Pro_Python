from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding="UTF_8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    new_list = []

# TODO 1: выполните пункты 1-3 ДЗ


def name_add():
    fio = r'([А-Я]{1}[а-яё]{1,23})'
    sub = r'\1'
    for column in contacts_list[1:]:
        line = column[0] + column[1] + column[2]
        if len((re.sub(fio, sub, line).split())) == 3:
            column[0] = re.sub(fio, sub, line).split()[0]
            column[1] = re.sub(fio, sub, line).split()[1]
            column[2] = re.sub(fio, sub, line).split()[2]
        elif len((re.sub(fio, sub, line).split())) == 2:
            column[0] = re.sub(fio, sub, line).split()[0]
            column[1] = re.sub(fio, sub, line).split()[1]
            column[2] = ''
        elif len((re.sub(fio, sub, line).split())) == 1:
            column[0] = re.sub(fio, sub, line).split()[0]
            column[1] = ''
            column[2] = ''

def phone_add():
    phone = r"(\+\d|\d)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})(\s\(?доб.\s\d+)?"
    # sub = r'+7(\3)\4-\5-\6\s\7'
    compiled2 = re.compile(phone)
    result2 = compiled2.match(str(w))
    # sub_result = re.sub(phone, sub, w) ПРИ ЗАМЕНЕ ВЫДАЁТ ГОРУ ОШИБОК, ПРОБЛЕМА В ЦИКЛЕ? Как вывести текст из списка в текст?
    # print(result2)


if __name__ == '__main__':
    for contact in contacts_list:
        if contact != new_list:
            new_list.append(contact)
    name_add()
    print(new_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)
