"""Ask the user to enter a password

Must not be empty.

Must be at least 8 characters.

Show custom error messages."""

raw_inputs = input("Please enter your password which should contain minimum 8 char: ")
password=raw_inputs.strip().replace (" ", "")
if raw_inputs == "":
    print("password cannot be blank")
elif len (raw_inputs.strip().replace(" ", "")) <8:
    print ("Too short. please enter a valid 8 characters long")
else:
    print ("Strong enough")

