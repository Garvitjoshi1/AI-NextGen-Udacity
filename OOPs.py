"""
Why Object-Oriented Programming?
Object-oriented programming has a few benefits over procedural programming, which is the programming style you most likely first learned. As you'll see in this lesson,

object-oriented programming allows you to create large, modular programs that can easily expand over time;
object-oriented programs hide the implementation from the end-user.

class - a blueprint consisting of methods and attributes
object - an instance of a class. It can help to think of objects as something in the real world like a yellow pencil, a small dog, a blue shirt, etc. However, as you'll see later in the lesson, objects can be more abstract.
attribute - a descriptor or characteristic. Examples would be color, length, size, etc. These attributes can take on specific values like blue, 3 inches, large, etc.
method - an action that a class or object could take
OOP - a commonly used abbreviation for object-oriented programming
encapsulation - one of the fundamental ideas behind object-oriented programming is called encapsulation:
            you can combine functions and data all into a single entity.
            In object-oriented programming, this single entity is called a class.
            Encapsulation allows you to hide implementation details much like how the scikit-learn package hides the implementation of machine learning algorithms.
"""


class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


Shirt('red', 'S', 'short sleeve', 15)

new_shirt = Shirt('red', 'S', 'short sleeve', 15)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_shirt.change_price(10)
print(new_shirt.price)

print(new_shirt.discount(.2))

tshirt_collection = []
shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve', 10)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)

for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color)

