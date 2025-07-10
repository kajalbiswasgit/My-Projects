"""Mini Practice Task (No Code Given)

Write a program that:
Asks the user to enter a PIN code
---Removes any spaces
---Validates that it is only 6 digits

Shows friendly error messages for:
---Blank input
---Letters or symbols entered
---Less or more than 6 digits
"""

pin_input=input("Please enter your pin (6 digits): ").strip().replace(" ", "")
if pin_input == "":
 print ("Pin cannot be blank")
elif not pin_input.isdigit():
 print ("Please enter a valid numeric digits only")
elif len(pin_input) !=6:
 print("Please enter a valid 6 digits pin only")
else:
 print("Pin validated")