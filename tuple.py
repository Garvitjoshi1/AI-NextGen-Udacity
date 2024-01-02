# Tuples are immutable data structures but are ordered.
dimensions = 52, 40, 100
#  three variables are assigned from the content of the tuple dimensions. This is called tuple unpacking.
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

# parenthesis are optional for making tuples
tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)  # therefore this condition is True.
print(tuple_a[1])
