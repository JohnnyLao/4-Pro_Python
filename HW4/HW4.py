nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class iterator:

    def __init__(self, new_list):
        self.new_list = [object for item in nested_list for object in item]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.new_list):
            raise StopIteration
        return self.new_list[self.cursor]


def generator(new_list_1):
    for item in new_list_1:
        for element in item:
            yield element


if __name__ == '__main__':

    print("ITERATOR:")
    for element in iterator(nested_list):
        print(element)

    print("GENERATOR:")
    for item_1 in generator(nested_list):
        print(item_1)
