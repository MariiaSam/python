# ТИПИ ДАНИХ

str = "Mariia" # строка

# Списки (Lists)
my_list = list()
empty_list = []
my_list = [1, 2, 3, 4, 5]
my_list = [1, "Hello", 3.14]
my_list.append(4)
my_list.remove("Hello")



# Кортежі (Tuples)
# Словники (Dictionaries)
# Множини (Sets)
# Заморожені множини (Frozen Sets)


message = "Hello world!"
print(message[0])
#===========================

name = "Oleg"
hello_string = f"Hello, {name}!"
print(hello_string)
#===========================

side_a = 10
side_b = 5

hypotenuse = (side_a**2 + side_b**2)**0.5
print(hypotenuse) # 11.180339887498949

S = side_a * side_b / 2
print(S) #25.0

#===========================
n = 5000

hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60

print(hours) # 1
print(minutes) # 23
print(seconds) # 20

#+==========================

x = 12
print(f"Значення x: {x}") # Значення x: 12

# a = input("Рядок запрошення: ")

age = input("How old are you? ")
age = int(age)

pi = float('3.14')

#==========================================
a = float(input("Введіть сторону квадрата a: "))
P = 4 * a
print(f"Периметр квадрата дорівнює {P}")


#==========================================

# Встановлюємо ціни на продукти
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Кількість кожного продукту
num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
total_cost = num_croissants * price_per_croissant + num_glasses * price_per_glass + num_coffee_packs * price_per_coffee_pack

# Визначаємо кількість повних доларів і центів
total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

# Вивід результату
print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
print(f"Загальна вартість у центах: {total_cents} центів")

#==========================================
