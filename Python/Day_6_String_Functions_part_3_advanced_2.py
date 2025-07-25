# Split and Validate Domain from Email
email= input ("please enter email:")
if "@" in email and "." in email:
    username, domain= email.split ("@")
    print ("username:",username)
    print ("domain:",domain)
    if domain.endswith (".com"):
        print ("its a corporate email")
    else:
        print ("its a normal domain")
else:
     print("Please enter a valid email")