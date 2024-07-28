import pickle

class Human:
    def __init__(self, name):
        self.name = name

bob = Human("Bob")
with open("instance.pickle", "wb") as file:
    pickle.dump(bob, file)
