#Requirements for a valid password:

"""
It should not be blank
At least 8 characters long
Must include at least one number
Must include at least one alphabet
No spaces allowed """


while True:
    password= input ("Please enter ur pass: ").strip ()
    if password == "":
     print ("cannot left blank")

    elif len(password) < 8:
     print ("must contain 8 digits")

    elif " " in password:
     print("Password should not contain spaces.")

    elif not any (char.isupper() for char in password):
     print ("password must contain atleast one upper letter")

    elif not any (char.isdigit() for char in password):
     print ("password must contain atleast a number")

    elif not any (char.isalpha() for char in password):
     print ("password must contain atleast a alphabetic char")
    else:
         print ("Best password")
         break