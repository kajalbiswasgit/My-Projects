"""Ask the user for their age and check if they are eligible for the following:
Under 13: Print "You are a child."
13 to 17: Print "You are a teenager."
18 to 59: Print "You are an adult."
60 and above: Print "You are a senior citizen."
🔒 Use a while True loop to ensure the user enters only numbers between 1 and 120. 
If not, show a friendly error message and ask again."""

age= None
while True: # Loop until a valid input is entered
    try:
        age= int(input("Please enter your age (1-120): "))
        if age < 1 or age > 120:
             print("Age must be between 1 and 120.")
             continue

        if age >= 1 and age <= 12:
               print ("You are a child.")
               break
        elif age >=13 and age <= 17:
               print ("You are a teenager.")
               break
        elif age >= 18 and age <= 59:
               print ("You are a adult.")
               break
        elif age >= 60:
               print ("You are a senior citizen.")
               break
        else:
              print("Please enter a valid age.")  
              break
              
    except ValueError:
        print ("Please enter a valid numeric digit.")

# Final confirmation
if age is not None:  # Show valid age
    print("✅ Thank you! Your age is:", age)
else:
    print("You did not enter a valid age.") # Should never reach here unless code changes