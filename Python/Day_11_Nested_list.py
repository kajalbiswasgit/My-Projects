# Nested list = A list inside another list
students = [
    ["Kajal", 87],     # students[0]
    ["Anu", 91],       # students[1]
    ["Riya", 95],      # students[2]
    ["Sneha", 78]      # students[3]
]
print(students[1]) # Go to index 1 → which is ["Anu", 91]
print(students[2][0]) # students[2] → means take the first item of that sublist → 'Riya'
print (students[3][1]) # students[3] → is ["Sneha", 78] [1] → means take the second item (index 1) from that sublist → 78
students.append (["Nayan", 87])
students.insert (1,["Jack", 46])
print ("students:",students)