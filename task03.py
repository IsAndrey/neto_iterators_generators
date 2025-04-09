class FlatIterator:

    def __init__(self, list_of_list):
        self.data = self.flat(list_of_list)
        self.max_counter = len(self.data)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        index = self.counter
        self.counter += 1
        if self.counter > self.max_counter:
            raise StopIteration
        return self.data[index]

    def flat(self, data):
        if isinstance(data, list):
            result = []
            for element in data:
                result.extend(self.flat(element))
        else:
            result = [data]

        return result


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
