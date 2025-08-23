#Create a dictionary for a book with keys: title, author, price, year.
"""Print only the author.
Add a new key publisher.
Update the price.
Delete the year.
Check if publisher exists in the dictionary."""

book = {"title":"ramayan","author":"kajal","price":"200","year":"1997"}
print ("Author:", book["author"])
print (book.get ("publisher"))
book ["publisher"] = "Biswas"
print (book["publisher"])
book ["price"] = 300
del book ["year"]
print ("Publisher".lower() in book)