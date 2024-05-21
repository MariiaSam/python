first_name = "John"
last_name = "Doe"


def get_fullname(first_name, last_name):

    get_fullname = first_name + " " + last_name
    return get_fullname


fullname = get_fullname("John", "Doe" )
print(fullname)

#=====================================
first_name = "Олексій"
last_name = "Гупало"
full_name = first_name + " " + last_name
print(len(full_name)) # 14

#=====================================
first_name = "Mariia"
last_name = "Samodurova"
full_name = first_name + " " + last_name
length = len(full_name)
print(full_name[0]) # M
print(full_name[length - 1]) #a
print(length) # 17

#=====================================

first_name = "John"
last_name = "Doe"


def get_initials(first_name, last_name):
    first_letter = first_name[0]
    full_name = last_name + ' ' + first_letter +'.'
    return  full_name 


formatted_name  = get_initials("John", "Doe")
print(formatted_name) # Doe J.

#=====================================

text = "  hello  "
print(text.strip()) # hello

#=====================================

first = "Python"
second = "python"



def compare(first, second):
        return first.upper() == second.upper()
    

result = compare("Python", "python")

#=====================================
text = "Hello, world!"
print(text.find("world")) # 7
print(text.find("Python"))  # -1

#=====================================
text = "I like cats"
new_text = text.replace("cats", "dogs")
print(new_text)  # I like dogs

#=====================================

text = "Hello, world! Welcome to the world of Python."

position = text.find("world")

updated_text = text.replace("world", "planet")
print(updated_text)

#=====================================

name = "Mariia"
age = 34
greeting = f"Мене звати {name}, і мені {age} років."
print(greeting) # Мене звати Mariia, і мені 34 років.


#=============================================

product_name = "Coffee Maker"
product_price = 7500.50
product_quantity = 15


def format_product_info(product_name, product_price, product_quantity):
    product_info = f"Product: {product_name}, Price: {product_price} UAH, Quantity: {product_quantity} pcs."
    return product_info


product_info = format_product_info("Coffee Maker", 7500.50, 15)
print(product_info)