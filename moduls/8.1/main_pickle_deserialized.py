import pickle

# Десеріалізація об'єкта з файлу
with open('data.pickle', 'rb') as file:
    deserialized_data = pickle.load(file)

# Виведе вихідний об'єкт Python
print(deserialized_data) # {'key': 'value', 'num': 100}
