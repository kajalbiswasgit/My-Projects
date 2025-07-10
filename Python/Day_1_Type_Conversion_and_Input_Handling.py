
#Concepts:
#Single-line comments use #
#Multi-line comments use triple quotes (''' or """)

#Convert data types with int(), float(), str()

#Handle bad input using try-except

try:
    age = int(input("Enter your age: "))
    print("You are", age, "years old.")
except ValueError:
    print("❌ Please enter a valid number.")
