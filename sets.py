# A set is a data type for mutable unordered collections of unique elements.
numbers = [1, 2, 3, 4, 5, 3, 2]
s = set(numbers)
print("Uniques elements only: ", s)

print(s.pop())  # to remove random element.
print(s.add(45))  # to add an element.

# Perform union, intersection, difference.
set1 = set(range(0, 100))
set2 = set(range(50, 100))
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

# Question
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
print(b)
