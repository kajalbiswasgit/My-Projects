#Ask user to enter an email address. Check:
"""It’s not blank
Has @ in it
Has no spaces"""
email= input ("Please enter ur email: ")
if email != "" and "@" in email and "." in email and " " not in email:
    print ("Its valid")
else:
    print ("provide a valid email")
