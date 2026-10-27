import math

def square(number):
    return math.ceil (number*number)

num = float(input("Введите длину стороны квадрата:"))
result = square(num)
print("площадь квадрата = ", result)

