#  Store the list of items in stock:
# ["Rice", "Sugar", "Salt", "Oil", "Soap", "Shampoo", "Biscuits"]

"""Tasks to perform:
Show the first item and the last item using indexing.
Show the middle three items using slicing.
Add a new item "Tea" to the list.
Remove "Salt" from the list.
Replace "Oil" with "Mustard Oil".
Print the final list"""

items_in_stock= ["Rice", "Sugar", "Salt", "Oil", "Soap", "Shampoo", "Biscuits"]
print(items_in_stock[0])
print(items_in_stock[-1])
print (items_in_stock[1::2])
items_in_stock.append("Tea")
items_in_stock.remove ("Salt")
items_in_stock.remove("Oil")
items_in_stock.insert (3,"Mustard oil")
print ("Final list:",items_in_stock)
for i in range (len(items_in_stock)):
    print (f"{i+1}. My updated items are {items_in_stock[i]}")