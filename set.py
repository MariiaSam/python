# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.count(5)

# print(x)
#2

# thistuple = (1, 3, 7, 8, 7, 5, 4, 8, 6, 8, 5)

# x = thistuple.count(8)

# print(x)

# #3


# thistuple = (8, 1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.index(8)

# print(x) #0


# fruits = {"apple", "banana", "cherry"}

# fruits.add("orange")

# print(fruits)

#{'orange', 'banana', 'cherry', 'apple'}


# fruits = {"apple", "banana", "cherry"}

# x = fruits.copy()

# print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)

print(z) # {'microsoft', 'google'}


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x) # {'banana', 'cherry'}


fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits) # {'apple', 'cherry'}


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z) # {'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z) #True Повертає відповідь, чи мають дві множини перетин

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z) # True Return True if all items in set x are present in set y:

def my_function():
  print("Hello from a function")

my_function() # Hello from a function

# class MyClass:
#   name = "John"

# del MyClass

# print(MyClass)

x = ["apple", "banana", "cherry"]

del x[0]

print(x) # ['banana', 'cherry']


#================================
# for i in range(-5, 5):
#   if i > 0:
#     print("YES")
#   elif i == 0:
#     print("WHATEVER")
#   else:
#     print("NO")

# NO
# NO
# NO
# NO
# NO
# WHATEVER
# YES
# YES
# YES
# YES
#================================

# x = 2
# if x > 3:
#   print("YES")
# else:
#   print("NO") 
#   NO

#================================

try:
  x > 3
except:
  print("Something went wrong")

  # Something went wrong



