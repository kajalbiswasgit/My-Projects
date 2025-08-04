#| Function Term | Meaning                                             |
"""
| ------------- | --------------------------------------------------- |
| `def`         | Keyword to define a function                        |
| `parameters`  | Variables that you pass inside the function         |
| `return`      | Sends back a value to where the function was called |
| Function call | Running the function with `()`                      |"""

# Create a function that takes a name and prints "Hello <name>!"
# Define the function with a parameter 'name'
def greet(name):
    print(f"Hello {name}!")
greet("Biswas")

# Create a function that adds two numbers and returns the result
def add(num1,num2):
    return (num1+num2)
result= add (40,50)
print ("sum is:", result)

# Create a function that multiplies 3 numbers and returns the answer
def multiply (num1,num2,num3):
    return (num1*num2*num3)
result = multiply (10,10,10)
print ("Multiply Result is:", result)

#Write a function that takes age and prints if the person is eligible to vote (18+)
def voter_age (age):
    if age >= 18:
        print ("You are eligible to vote")
    else:
        print("You are not eligible to vote")
voter_age (17)
voter_age (26)

# Function that returns the square of a number
def square(num):
    return num * num

print("Square is:", square(6))

# Create a function introduce that accepts two arguments: name and profession
def introduce (name,profession):
    print (f"hi,i am {name}.Working as {profession}.")
introduce ("kajal","Tester")

#Task: Create a function greet_by_time(name, time) that prints:

# "Good morning, Kajal!" if time is "morning"
# "Good evening, Kajal!" if time is "evening"
def greet_by_time (name,time):
    time=time.lower ()
    if time == "morning":
        print (f"Good morning,{name}!")
    elif time == "evening":
        print (f"Good evening,{name}!")
    else:
        print (f"Have a good day,{name}!")
greet_by_time ("kajal","Morning")
