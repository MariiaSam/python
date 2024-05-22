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
