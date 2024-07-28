'''import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}

# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(serialized_data)   # b'\x80\x04\x95\x1b\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x03key\x94\x8c\x05value\x94\x8c\x03num\x94K*u.'

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(deserialized_data) # {'key': 'value', 'num': 42}

'''

import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 100}

# Серіалізація об'єкта в файл
with open("data.pickle", "wb") as file:
    pickle.dump(my_data, file)
