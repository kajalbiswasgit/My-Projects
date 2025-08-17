#| Function/Concept| Description                                   |
"""
| ---------------- | ---------------------------------------------- |
| `()`             | Used to define a tuple.                        |
| `tuple()`        | Converts other types (like list) into a tuple. |
| `len(tuple)`     | Returns the number of elements in the tuple.   |
| `tuple[index]`   | Access an item by index (starts from 0).       |
| `count(value)`   | Counts how many times a value appears.         |
| `index(value)`   | Returns the first index of the value.          |"""
# Q18. Tuple of students: (name, (maths, science))
students = [
    ("Kajal", (88, 92)),
    ("Amit", (78, 85)),
    ("Sneha", (90, 95))
]

# Print full data of Amit
print("Full data of amit:", students[1])

# Print Kajal's science marks
print("Kajal's science marks:", students[0][1][1])

# Print all student names using loop
for i in range (len(students)):
    print (f"{i+1}. My top students are {students[i][0]}")
