import pickle

class Human:
    def __init__(self, name):
        self.name = name

with open("instance.pickle", "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name)
