# List are mutable data types
list = [2, 3, 4, 5, 6, 7]
# printing the index
print(list[0])
# slicing
print(list[:4])
# moves till last-1
print(list[2: 5])
""" Membership Operator : in or not in"""
list = ["Jan", "Feb", "March", "April", "May", "June", "July"]
print("June" in list)
print("Feb" not in list)
print("Sunday" in list)
""" List are mutable and string's are not, but they both are ordered"""

scores = ["B", "C", "A", "D", "B", "A"]
grades = scores
print("Scores: "+str(scores))
print("Grades: "+str(grades))

print(len(scores))
print(max(scores))
print(min(scores))
print(sorted(scores))

'''Join method'''
direction = "\n.join(['North', 'South', 'East', 'West'])"
print(direction)

name = "-".join(['Hi', "Hello", "User"])
print(name)
