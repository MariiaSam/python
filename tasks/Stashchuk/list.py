# 1.


list_element = [1, True, 'one', None, 'apple']


# 2.
list_element.pop(2)
print(list_element)  # [1, True, None, 'apple']

# 3
print(len(list_element))  # 4

# 4
list_element.reverse()
print(list_element)

# 5
b = [3, 'banana']

# 6
list_element.extend(b)
print(list_element)  # ['apple', None, True, 1, 3, 'banana']
