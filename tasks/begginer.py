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


