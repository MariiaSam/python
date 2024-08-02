'''
Розробіть програму-резюме, яка за введеними початковими даними і порядковим номером виводить таку інформацію: 1 - прізвище, 2 - ім’я, 3 - вік, 4 - хобі, 5 - номер телефону.

Вхідні дані:

Brendan
Eich
57
programmer
4567231
4
Вихідні дані:

Programmer
'''

def program_resume(n):
   match n:
      case 1: return "Brendan"
      case 2: return "Eich"
      case 3: return 57
      case 4: return "programmer"
      case 5: return 4567231
      case 6: return 4
      case _: return "?????"
print (program_resume(4))

# programmer

# 2 var

def program_resume_second_var(n):
    surname = "Brendan"
    name = "Eich"
    age = 57
    hobby = "programmer"
    phone_number = "4567231"

    if n == 1:
        return surname
    elif n == 2:
        return name
    elif n == 3:
        return age
    elif n == 4:
        return hobby
    elif n == 5:
        return phone_number
    else:
        return "Invalid input"

input_data = ["Brendan", "Eich", 57, "programmer", "4567231", 4]

n = input_data[-1]

print(program_resume_second_var(n))


# 3 var

def  program_resume_third_var():
    user_data = {}
    user_data["last_name"] = input("Введіть прізвище: ")
    user_data["first_name"] = input("Введіть ім'я: ")
    user_data["age"] = int(input("Введіть вік: "))
    user_data["hobby"] = input("Введіть хобі: ")
    user_data["phone"] = input("Введіть номер телефону: ")

    return user_data

def print_resume_item(user_data, item_number):
    items = ["last_name", "first_name", "age", "hobby", "phone"]
    if item_number > 0 and item_number <= len(items):
        return user_data[items[item_number - 1]]
    else:
        return "Неправильний номер пункту"

user_info =  program_resume_third_var()

item_to_print = int(input("Введіть номер пункту для виведення (1-5): "))
result = print_resume_item(user_info, item_to_print)
print(result)


