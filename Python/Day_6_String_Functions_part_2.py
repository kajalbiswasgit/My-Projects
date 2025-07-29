# Write a Python program to validate a user’s phone number based on the following rules:
"""It must not be blank

It must contain only digits

It must be exactly 10 digits long

It must not start with 0"""



phone = input("Enter your phone number: ").strip()  
# Asks user to enter number, removes any spaces around

if phone == "":
    print("Phone number cannot be blank.")  
# Condition 1 – Not empty

elif not phone.isdigit():
    print("Phone number must contain only digits.")  
# Condition 2 – Must be all digits

elif len(phone) != 10:
    print("Phone number must be exactly 10 digits.")  
# Condition 3 – Length check

elif phone.startswith("0"):
    print("Phone number cannot start with 0.")  
# Condition 4 – Starting digit check

else:
    print("Phone number is valid.")  
# Final success message
