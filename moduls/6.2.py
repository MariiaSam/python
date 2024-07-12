from collections import UserDict

class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value

# Створення екземпляра власного класу
my_dict = MyDictionary({'a': 1, 'b': 2})
my_dict.add_key('c', 3)
print(my_dict)


# =====================================

from collections import UserList
from random import randint

class ExperimentsResults(UserList):

    def positive_values(self):
        return list(filter(lambda x: x >= 0, self.data))

    def negative_values(self):
        return list(filter(lambda x: x < 0, self.data))


result = ExperimentsResults()

for _ in range(20):
    result.append(randint(-10, 10))

print(result)
print(result.positive_values())
print(result.negative_values())
print(result.data)


#==============================
from collections import UserDict


class DualDict(UserDict):
    def __init__(self, initial=None):
        if initial is None:
            self.from_value = dict()
            self.data = dict()
        else:
            self.data = initial
            self.from_value = {val: key for key, val in initial.items()}

    def __setitem__(self, key, value):
        self.data[key] = value
        if value in self.from_value:
            old = self.from_value[value]
            self.from_value.pop(old)
        self.from_value[value] = key

    def get_by_value(self, value):
        return self.from_value[value]

    def set_by_value(self, value, key):
        old_key = self.from_value[value]
        self.data.pop(old_key)
        self.data[key] = value
        self.from_value[value] = key

dual = DualDict({1:2, 3:4})
print(dual)
print(dual.get_by_value(2) == 1)
dual.set_by_value(4, 8)
print(dual)
