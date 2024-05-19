my_dict = {"name": "Олексій", "age": 30}

print(my_dict) # {'name': 'Олексій', 'age': 30}

# ==============================

my_dict = {"name": "Олексій", "age": 30}

print(my_dict["name"]) # Олексій

print(my_dict["age"]) # 30

# ==============================

my_dict = {"name": "Олексій", "age": 30}

my_dict["age"] = 31

print(my_dict) # {'name': 'Олексій', 'age': 31}

# ==============================
my_dict = {"name": "Олексій", "age": 31}

my_dict["email"] = "oleksiy@gmail.com"

print(my_dict) # {'name': 'Олексій', 'age': 31, 'email': 'oleksiy@gmail.com'}

# ==============================

my_dict = {"name": "Олексій", "age": 31, "email": "oleksiy@gmail.com"}
del my_dict["email"]
print(my_dict)
