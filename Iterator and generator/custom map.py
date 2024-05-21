class CustomMapIter:

    def __init__(self, iterable: dict, func1, func2):
        self.iterable = iterable
        self.func1 = func1
        self.func2 = func2
        self._keys = iter(iterable.keys())

    def __iter__(self):
        return self

    def __next__(self):
        try:
            key = next(self._keys)
            new_key = self.func1(key)
            new_value = self.func2(self.iterable[key])
            return new_key, new_value
        except StopIteration as ex:
            raise ex

my_dict = {}
for i in range(1, 6):
    my_dict[f'key{i}'] = f'value{i}'

print(list(CustomMapIter(my_dict, lambda x: x * 2, lambda y: y * 2)))
