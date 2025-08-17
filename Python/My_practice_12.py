#Tasks:
"""Find all unique students who are enrolled in either Python or Java.
Find students who are enrolled in both Python and Java.
Find students who are only in Python but not in Java.
Find students who are only in Java but not in Python.
Find students who are in exactly one course (but not both).
Check if all Python students are also in Java.
Chck if all students in either batch combined cover all Java students.
Check if Python and Java batches have no students in common."""

batch_python = {"Amit", "Riya", "Kajal", "Rahul", "Sneha", "Pooja"}
batch_java = {"Riya", "Vikram", "Sneha", "Kajal", "Aman", "Suman"}

# 1. Unique students (either Python or Java)
unique_students = batch_python.union(batch_java)
print("Unique students:", unique_students)

# 2. Students in both courses
students_in_both = batch_python.intersection(batch_java)
print("Students in both Python and Java:", students_in_both)

# 3. Only in Python
only_python = batch_python.difference(batch_java)
print("Only Python students:", only_python)

# 4. Only in Java
only_java = batch_java.difference(batch_python)
print("Only Java students:", only_java)

# 5. Exactly one course (but not both)
exactly_one_course = batch_python.symmetric_difference(batch_java)
print("Students in exactly one course:", exactly_one_course)

# 6. Check if all Python students are also in Java
all_python_in_java = batch_python.issubset(batch_java)
print("All Python students are also in Java:", all_python_in_java)

# 7. Check if combined students cover all Java students
combined_students = batch_python.union(batch_java)
all_combined_cover_java = combined_students.issuperset(batch_java)
print("Combined students cover all Java students:", all_combined_cover_java)

# 8. Check if no students are in both
no_common_students = batch_python.isdisjoint(batch_java)
print("No students in both Python and Java:", no_common_students)
