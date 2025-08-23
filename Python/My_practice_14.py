# Create a dictionary named product with keys:
"""
"id" → "P101"
"name" → "Wireless Mouse"
"price" → 750
"stock" → 120
"category" → "Electronics"
Print only the product name.
Add a new key "discount" with value 10 (percentage).
Update the stock after selling 5 units.
Delete the "category" key.
Check if "discount" exists in the dictionary """
product = {"id":"P101","name":"Wireless Mouse","price":750,"stock":120,"category":"electronics"}
print ("Product name:",product ["name"])
product ["discount"]=10
print ("Discounted added:",product["discount"],"%")
discounted_price= product ["price"] - (product["price"] * product ["discount"]/100)
product ["stock"]= 120-5
print ("Updated stock:",product["stock"])
del product["category"]
print ("Discount is available:", "discount".lower() in product)
print ("Price after discount:",discounted_price)