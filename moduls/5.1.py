# from collections import namedtuple

# # Створення іменованого кортежу
# Point = namedtuple('Point', ['x', 'y'])


# # Створення екземпляра Point
# p = Point(11, y=22)

# # Доступ до елементів
# print(p.x)  # 11
# print(p.y)  # 22

#======================================= Створення іменованого кортежу
# import collections

# Person  = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# print(person.first_name) # Mick
# print(person[3]) # Boston

#=========================
# import collections

# Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

# cat = Cat('Simon', 4, 'Krabat')

# print(f'This is a cat {cat[0]}, {cat.age} age, his owner {cat[2]}')

# This is a cat Simon, 4 age, his owner Krabat


#======================================= Counter
'''Counter функціонує як словник, де ключами є елементи, а значеннями - їх кількість у колекції.
'''

# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)

# # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})

# print(mark_counts.most_common()) # [(4, 4), (6, 3), (1, 3), (2, 2), (7, 2), (3, 2), (5, 2)]
# print(mark_counts.most_common(1)) # [(4, 4)]
# print(mark_counts.most_common(2)) # [(4, 4), (6, 3)]

#======================
# from collections import Counter

# # Створення Counter з рядка
# letter_count = Counter("banana")
# print(letter_count) # Counter({'a': 3, 'n': 2, 'b': 1})


#======================
# from collections import Counter


# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_count = Counter(words)

# # Виведення слова та його частоти
# for word, count in word_count.items():
#     print(f"{word}: {count}")


'''the: 2
quick: 1
brown: 1
fox: 1
jumps: 1
over: 1
lazy: 1
dog: 1'''


from collections import defaultdict

# Створення defaultdict з list як фабрикою за замовчуванням
# d = defaultdict(list)

# # Додавання елементів до списку для кожного ключа
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)

# print(d)
# # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})

#======================================
d = defaultdict(int)

# Збільшення значення для кожного ключа
# d['a'] += 1
# d['b'] += 1
# d['a'] += 1

# print(d)
# defaultdict(<class 'int'>, {'a': 2, 'b': 1})

#======================================

# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(dict(grouped_words))
# # {'a': ['apple', 'appendix'], 'z': ['zoo'], 'l': ['lion', 'lama'], 'b': ['bear', 'bet'], 'w': ['wolf']}

#======================================

# from collections import deque

# # Створення черги
# queue = deque()

# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')

# print("Черга після додавання елементів:", list(queue)) # ['a', 'b', 'c']

# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft()) # a

# print("Черга після видалення елемента:", list(queue)) # ['b', 'c']

# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0]) # b

# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0) # False

# # Size: Розмір черги
# print("Розмір черги:", len(queue)) # 2

#======================================
# from decimal import Decimal

# print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
# print(Decimal("0.1") + Decimal("0.2"))

'''
True
0.3
'''

# from decimal import Decimal, getcontext

# getcontext().prec = 6
# print(Decimal("1") / Decimal("7")) # 0.142857

# getcontext().prec = 8
# print(Decimal("1") / Decimal("7")) # 0.14285714


# ============================================= Якщо ми потребуємо саме округлення чисел, нам необхідно використовувати метод quantize

# from decimal import Decimal, ROUND_DOWN

# Вихідне число Decimal
# number = Decimal('3.14159')

# Встановлення точності до двох знаків після коми
# rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

# print(rounded_number)
# 3.14''

# =============================================
# import decimal
# from decimal import Decimal
 
# number = Decimal("1.45")

# # Округлення за замовчуванням до одного десяткового знаку
# print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0"))) # 1.4

# # Округлення вверх при нічиї (ROUND_HALF_UP)
# print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP)) # 1.5

# # Округлення вниз (ROUND_FLOOR)
# print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR)) # 1.4

# # Округлення вверх (ROUND_CEILING)
# print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING)) # 1.5

# # Округлення до трьох десяткових знаків за замовчуванням
# print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000"))) # 3.142


# =============================================

# def count_down(start):
#     while start > 10:
#         yield start
#         start -= 1

# for number in count_down(5):
#     print(number)

'''
5
4
3
2
1
'''
