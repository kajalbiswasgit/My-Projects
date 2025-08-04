#| Function    | Description                                                |
"""| ----------- | ---------------------------------------------------------- |
| `append()`  | Adds a new item to the **end** of the list                 |
| `insert()`  | Inserts an item at a **specific position**                 |
| `pop()`     | Removes the **last item** (or item at index) from the list |
| `sort()`    | Sorts the list in **ascending order** (numbers or strings) |
| `reverse()` | Reverses the **order** of the list (not alphabetically!)   |"""

# Task 1: Student Scores
"""# Create a list of marks
marks = [56, 87, 45, 92]

# Add a new mark using append
# Insert a mark at index 2
# Remove the last mark using pop
# Sort the list
# Reverse the list
# Print at every step
"""
marks = [56,87,45,92]
marks.append(100)
print ("Updated marks:", marks)
marks.insert(1,59)
print ("Updated marks:", marks)
removed_mark= marks.pop (1)
print ("Removed mark:", removed_mark)
print ("Updated marks:", marks)
marks.sort()
print ("sorted marks:", marks)
marks.reverse()
print ("Reverse marks:", marks)