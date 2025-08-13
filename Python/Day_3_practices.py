# Practice 1: Age Validator
"""Ask the user for their age and keep asking until they enter a valid number between 1 and 120.
       Then print if they are a child (<13), teenager (13-19), adult (20-59), or senior (60+)."""
while True:
    try:
        age =int (input("what is your age: "))
        if age >= 1 and age <= 120:
            break
        else:
            print("Please enter an age between 1 and 120.")
    except ValueError:
        print ("Invalid input. Please enter a number only")

print("Thank you! Your age is:", age)