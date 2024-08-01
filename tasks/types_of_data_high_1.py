# 1
'''

Дано ціле число n. Виведіть наступне за ним парне число.

Вхідні дані:

7
10
11
Вихідні дані:

8
12
12'''

'''number = int(input("Enter a number: "))

if number % 2: # є ненульовою
    print(number+1)
else:
    print(number+2)
'''

'''
8
12
12
'''

# 2

'''
Равлик повзе по вертикальній жердині висотою h метрів, піднімаючись за день на a метрів, а за ніч спускаючись на b метрів. На який день равлик доповзе до вершини жердини? Дані вводяться у порядку h, a, b.

Вхідні дані:

10
3
2
Вихідні дані:

8
'''

def days_to_reach_height(height, day_climb, night_descent):
    current_height = 0
    days = 0

    while True:
        days += 1
        current_height += day_climb
        if current_height >= height:
            break
        current_height -= night_descent

    return days

height = 10
day_climb = 3
night_descent = 2

result = days_to_reach_height(height, day_climb, night_descent)
print(result)  

    