# A dictionary is a mutable data type that stores mappings of unique keys to values
elements = {"hydrogen": 1, "helium": 2, "carbon": 6, "lithium": 3}
print(elements)
print("hydrogen" in elements)
print(elements.get("oxygen"))  # to extract the key.

# Identity Operators:- is, is not
x = elements.get("oxygen")
not_null = x is not None
print(not_null)
