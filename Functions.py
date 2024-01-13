import math


def cylinder_volume(height, radius):
    pi = math.pi
    volume = height * pi * radius ** 2
    return volume


print(cylinder_volume(10, 3))


def print_greeting():
    print("Hello World!")


print_greeting()  # no need to use print function because no return present.

''' Lambda Expression : Used to create an anonymous function'''


def multiply(x):
    return x * 2


print(multiply(3))

# above code reduced to
y = lambda x: x * 2
print(y(8))

multiply = lambda x, z: x * z
print(multiply(2, 3))
