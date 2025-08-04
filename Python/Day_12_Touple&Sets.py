#| Function/Concept | Description                                  | Example                       |
"""| ---------------- | -------------------------------------------- | ----------------------------- |
| `tuple()`        | Creates a tuple (immutable list)             | `my_tuple = tuple([1, 2, 3])` |
| `len()`          | Returns length                               | `len(my_tuple)`               |
| `count()`        | Counts how many times a value appears        | `my_tuple.count(2)`           |
| `index()`        | Finds the index of a value                   | `my_tuple.index(3)`           |
| `set()`          | Creates a set (unique values only)           | `my_set = set([1, 2, 2, 3])`  |
| `add()`          | Adds item to set                             | `my_set.add(4)`               |
| `remove()`       | Removes item from set (error if not present) | `my_set.remove(2)`            |
| `discard()`      | Removes item (no error if not found)         | `my_set.discard(10)`          |
| `union()`        | Combines two sets                            | `set1.union(set2)`            |
| `intersection()` | Common values in sets                        | `set1.intersection(set2)`     |
| `difference()`   | Values in set1 not in set2                   | `set1.difference(set2)`       |"""

# Remove Duplicates from a List
nums = [4, 6, 4, 6, 7, 8, 4, 9]
updated_nums = set (nums)
print ("Updated num:",updated_nums)

# Find Common Students in Two Batches
batch_A = {"Rita", "Rahul", "Simran", "Anita"}
batch_B = {"Anita", "Ravi", "Simran", "John"}
common= batch_A.intersection(batch_B)
print ("Common:",common)

# Combine Unique Languages
python_devs = {"Ravi", "Anu", "Simran"}
java_devs = {"Ravi", "Karan", "John"}
combine= python_devs.union(java_devs)
print ("combined:",combine)

# Find Students Who Only Know Python
python_devs = {"Ravi", "Anu", "Simran"}
java_devs = {"Ravi", "Karan", "John"}
python_devs= python_devs.difference(java_devs)
print("Python devs:",python_devs)

# Symmetric Difference – Uncommon Elements
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
uncommon= A.symmetric_difference(B)
print ("Uncommon:",uncommon)

# Numbers in one set but not both
set1 = {1, 2, 3, 5, 7}
set2 = {3, 5, 6, 8}
uncommon_set= set1.symmetric_difference(set2)
print ("Uncommon:",uncommon_set)

# Q2. Modify the set below to:
# a. Add "grape"
# b. Remove "banana"
fruits = {"apple", "banana", "cherry"}
fruits.remove ("banana")
fruits.add ("grape")
print ("fruits",fruits)