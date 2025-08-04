# Take a user input sentence and:
"""Convert to lowercase and print.
Replace any spaces with underscores.
Check if it ends with a period (.)"""

message= input ("please enter ur message: ").lower().strip()
modified_message= message.replace (" ","_")

if message.endswith ("."):
        print ("Correct message")
        print ("Modified message:",modified_message)
else:
        print ("Message must ends with a.")