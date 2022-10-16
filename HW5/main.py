import os
from decor import logging

path = os.path.join(os.getcwd(), 'log.txt')

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


@logging(path)
def generator(new_list):
    for item in new_list:
        for item1 in item:
            yield item1


if __name__ == '__main__':
    for item in generator(nested_list):
        print(item)