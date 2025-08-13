# Day 3 – Input Validation & Basic String Functions
# strip() — What does it do? - It removes the spaces before and after, but not between words.
# replace() Function — What is it? This removes all the spaces by replacing " " with an empty string "".
"""
 msg = "apple banana apple"
print(msg.replace("apple", "orange"))
# Output: "orange banana orange """

# lower() / upper() -- Converts string to all lowercase or uppercase

# isdigit() -- Returns True if the input is a number only (0–9).

# len() -- Returns the number of characters in a string.
"""name = "Kajal"
print(len(name))  # ➜ 5
"""

# Mini Task 1: Check mobile number
""" 🧠 Goal: Accept a mobile number and check:
It should be exactly 10 digits
It should contain only numbers (no letters or symbols)"""

mobile= input ("Please enter a valid 10 digits mobile no: ").strip().replace(" ", "")

if mobile.isdigit () and len (mobile) ==10:
  print ("Its a valid phone no")
else:
 print ("Please enter a valid 10 digit phone no ")