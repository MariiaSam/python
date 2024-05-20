my_dict = {"name": "Олексій", "age": 31}

if my_dict["age"] >= 18:
    print("Ви повнолітній")


#========================================
condition = 0

if condition ==0:
    value = 10


#========================================

my_dict = {"name": "Андрій", "age": 16}

if my_dict["age"] >= 18:
    print("Ви повнолітній")
else:
    print("Вибачте, ви ще не маєте права голосу")

#========================================

condition = 7

if condition >= 13:
    value = 10
else:
    value = 20

#========================================
first = 10
second = 5
expression = (((first + second) ** 3) + ((first - second) ** 2) )// 3

print(expression)

#========================================

first = 10
second = 5

sum_result = (first + second) ** 3

difference_result = (first - second) ** 2

total_result = sum_result + difference_result

expression = total_result // 3
print(expression)
#========================================

data = []

data.insert(0, 1)         
data.insert(1, "python")  
data.insert(2, 3.11)   
print(data)