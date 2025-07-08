"""✅ Task 1: Simple Loop with Numbers"""
#Print numbers 1 to 5 using a for loop and f-string.

for i in range(1, 6):  # Loop from 1 to 5
    print(f"{i}. Number is {i}")  # Embed value of i inside the f-string

"""✅ Task 2: You have a list of your favorite fruits. Use a for loop and f-string to print them one by one with numbering."""

fruits = ["Mango", "Banana", "Apple", "Grapes"]

for i in range(len(fruits)):
    print(f"{i+1}. I like {fruits[i]}")
 

