# Zip() function in Python is a built-in function that takes two or more iterables (lists, tuples, sets, etc.
# Merge two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
zipped_list = zip(list1, list2)
print(zipped_list)
# print(list(zipped_list))  # give error to perform below action.

a, b = zip(*zipped_list)
print(a, "\n", b)

# Enumerate is a built-in function that returns an iterator of tuples containing indices and values of a list.
num = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for i, j in enumerate(num):
    print(i, j)
# i am index value
# j in num in iterated form
