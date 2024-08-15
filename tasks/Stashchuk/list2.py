# 1
a = [1, "one", "where do you live?", True]
b = [2, None, 'So-so']

# 2
c = a + b
print(c)  # [1, 'one', 'where do you live?', True, 2, None, 'So-so']

# 3
print(dir(c))
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

# 4
c = a.__add__(b)
print(c)

# 5  # [1, 'one', 'where do you live?', True, 2, None, 'So-so']
