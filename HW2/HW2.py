from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding="UTF_8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    new_list = []

# TODO 1: выполните пункты 1-3 ДЗ
def name_add():
    fio = r'([А-Я])'
    sub = r' \1'
    for column in contacts_list[1:]:
        # pprint(column)
        line = column[0] + column[1] + column[2]
        print(line)
        print(len((re.sub(fio, sub, line).split())))
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
    return


def phone_add():
    phone = re.compile(r'(\+\d|\d)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})(\s\(?доб.\s\d+)?')
    sub = r'+7 (\3) \4-\5-\6 \7'
    for column in contacts_list:
        column[5] = phone.sub(sub, column[5])
    return


def dup():
    for column in contacts_list[1:]:
        first_name = column[0]
        last_name = column[1]
        for contact in contacts_list:
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if column[2] == '':
                    column[2] = contact[2]
                if column[3] == '':
                    column[3] = contact[3]
                if column[4] == '':
                    column[4] = contact[4]
                if column[5] == '':
                    column[5] = contact[5]
                if column[6] == '':
                    column[6] = contact[6]
    for contact in contacts_list:
        if contact != new_list:
            new_list.append(contact)
    return


if __name__ == '__main__':
    name_add()
    phone_add()
    dup()
    # print(new_list)


# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)
