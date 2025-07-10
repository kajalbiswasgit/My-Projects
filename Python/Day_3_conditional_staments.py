""". What are Conditional Statements?
This allows your program to make decision based on the conditions
Think of it like:

“If its raining, take an umbrella.”

“If user entered the right password, login success. Else, show error
"""

# if Statement Syntax
#if condition:
    # do this if condition is True

# else Block
# Use else when you want to run something if the condition is False.

while True:
    try:
        age=int(input ("What is your age: "))
        break
    except ValueError:
        print("Please enter a valid input.")

if age >= 18:
   print ("You are adult now")
else:
    print ("you are a minor now")
