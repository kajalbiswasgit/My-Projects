#Task 2: Validate Aadhaar Number

#Condition:

# Ask the user to enter their Aadhaar number.

"""
✅ Must be 12 digits long
✅ Must contain only digits
✅ Should not accept spaces or characters
"""

aadhar_number =input ("Please enter your 12 digit aadhar number: ").strip().replace (" ", "")
if aadhar_number == "":
    print ("Aadhar number cannot be blank")
elif not aadhar_number.isdigit ():
    print ("Please enter in digits only")
elif len(aadhar_number) != 12:
    print ("Please enter a valid 12 digits long")
else:
    print ("Addhar is validated")