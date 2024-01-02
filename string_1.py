# we can use single and double quote both to print a string

salesman = "I think you 'are' an encyclopedia salesman"
# to write something in double quote inside use either-or.
print(salesman)

salesman = "I think you \n are an encyclopedia salesman"
# /n for new line
print(salesman)

salesman = ' "To print something in double quote or use alternate" '
print(salesman)
print(len(salesman))

# concatenation
print(salesman + "hello world!")

# print(len(234)) gives error as integer has no len

# f-string method
a = 10
b = 20
c = a + b
print("Sum of {a} and {b} is {c}")

# to print first alphabet of word capital
print(salesman.title())

# to count number of times a word occur in string
print(salesman.count("in"))

# to find word end at what index in String.
print(salesman.find('or'))

# split method
salesman = "I think you are an encyclopedia salesman"
print(salesman.split())
print(salesman.split(' ', 3))
print(salesman.split('.'))

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print("Length of verse is: ", len(verse))
print(verse.find("and"))
print(verse.rfind("you"))
print(verse.count("you"))
