# 1.Напишіть програму, яка отримує три цілих числа, введені з клавіатури (кожне число вводиться на окремому рядку), і друкує на екрані їх суму, добуток, результат піднесення першого числа до степеня різниці другого і третього чисел.

# Вхідні дані:

# 2
# 3
# 6


# Вихідні дані:

# 11
# 36
# 0.125

first_numb = int(2)
second_numb = int(3)
third_numb = int(6)

print(first_numb)
print(second_numb)
print(third_numb)

total_sum = first_numb + second_numb + third_numb

print(total_sum) # 11

total_mult = first_numb * second_numb * third_numb
print(total_mult) # 36

diff = (second_numb - third_numb)
total_diff = first_numb ** diff
print(total_diff)


# 2. Напишіть програму, яка приймає ціле число n і обчислює значення виразу n + nn + nnn.

# Вхідні дані:

# 5
# 3
# 1

# Вихідні дані:

# 615
# 369
# 123

first_numb = int(5)
second_numb = int(3)
third_numb = int(1)

# 5 + 55 + 555 = 615

nn_numb = str(first_numb)+str(first_numb)
nnn_numb = str(first_numb)+str(first_numb) + str(first_numb)
print(nn_numb) # 55
print(nnn_numb) #555

result = first_numb + int(nn_numb) + int(nnn_numb)
print(result) # 615


# 3. Напишіть програму, яка отримує такі дані: ім’я, вік, хобі, введені з клавіатури (вводяться на окремих рядках), і друкує на екрані одним повідомленням повну інформацію на основі введених даних.

# Вхідні дані:

# Lord Voldemort
# 72
# Magic
# Вихідні дані:

# My name is Lord Voldemort. I am 72 and my hobby is Magic.

name = "Lord Voldemort"
age = 72
hobby = "Magic"

str = "My name is " + name + ". I am " + str(int(age)) + " and my " + "hobby is " + hobby 
print(str)

# 4. Напишіть програму, яка зчитує довжину основи та висоту прямокутного трикутника (цілі числа), обчислює площу і друкує її значення на екрані у відформатованому вигляді (два символи після десяткової крапки). Кожен параметр вводиться на окремому рядку.

# Вхідні дані:

# 3
# 4
# Вихідні дані:

# 6.00

length = int(3)
print(length)

heigth = int(4)
print(heigth)

total = 0.50 * length * heigth
print(f"{total:.2f}") 

