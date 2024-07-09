# 1.
'''
Напишіть програму для друку дробових чисел у форматі до 2 десяткових знаків.

Вхідні дані:

3.1415926
1.4567
5.8
Вихідні дані:

3.14
1.46
5.80

'''

# def float_numbers(number):
#     value = round(number, 2)
#     print(value)

# result = float_numbers(3.1415926)
# result = float_numbers(1.4567)
# result = float_numbers(5.8)

'''
3.14
1.46
5.8
'''

def float_numbers(number):
    value = f"{number:.2f}"
    print(value)

result = float_numbers(3.1415926)
result = float_numbers(1.4567)
result = float_numbers(5.8)

'''
3.14
1.46
5.80
'''

