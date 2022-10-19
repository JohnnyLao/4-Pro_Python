from decor import decor, parametrized_decor


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


@decor
def generator(new_list):
    for item in new_list:
        for item1 in item:
            yield item1


@parametrized_decor("log.txt")
def generator(new_list):
    for item in new_list:
        for item1 in item:
            yield item1


if __name__ == '__main__':

    for item in generator(nested_list):
        print(item)


