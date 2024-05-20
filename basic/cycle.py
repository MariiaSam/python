fruits = ["яблуко", "банан", "вишня"]
for fruit in fruits:
    print(fruit)


# яблуко
# банан
# вишня

#=====================================for letter in "Python":
for letter in "Python":
    print(letter)

# P
# y
# t
# h
# o
# n

#=====================================
sentence = "The quick brown fox jumps over the lazy dog"
length = 0
for i in sentence:
    if i != ' ':    
        length = length + 1

    print(":", length)

#=====================================

for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

for i in range(1, 10, 2):
    print(i)

# 1
# 3
# 5
# 7
# 9

#=====================================
summary = 0

for i in range(1, 101):
    summary = summary + i

    print(summary) # 5050

#=====================================
count = 0
while count < 5:
        print("Число:", count) # Число: 0
# Число: 1
# Число: 2
# Число: 3
# Число: 4
        count = count + 1

#=====================================

N = 10
sum_squares = 0
i = 1
while i <= N:
    sum_squares += i * i 
    i = i + 1

print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}")
