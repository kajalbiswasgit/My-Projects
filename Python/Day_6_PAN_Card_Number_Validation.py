# PAN Card Number Validation (Important for Automation Testing Forms)
"""
✅ Requirements:
Must be exactly 10 characters long

First 5 characters must be uppercase letters

Next 4 characters must be digits

Last 1 character must be an uppercase letter

No spaces allowed"""
pan= input ("Please enter ur pan no:").strip()
if pan=="":
    print ("Pan cannot be blank")
elif len (pan) !=10:
    print ("must be 10 digits")
elif not (pan [:5].isalpha() and pan [:5].isupper()):
    print ("first 5 letter must be alphabatic and capital")
elif not (pan [5:9].isdigit()):
    print ("Middle letter will be in digits only")
elif not (pan [9].isalpha() and pan [9].isupper()):
    print ("Last letter must be alphabatic and capital")
elif " " in pan:
    print ("Space not allowed")
else:
    print ("Its a valid pan card")
