# Start with this list:
orders = ["Pizza", "Burger", "Pasta", "Salad", "Burger"]
orders.append ("Fries")
orders.insert (2,"Soup")
orders.extend (["Ice Cream","Sandwich"])
orders.pop(orders.index("Burger"))
removed_order= orders.pop(3)
print ("total burger remains:",orders.count("Burger"))
orders.sort ()
orders.reverse()
print (orders)
backup_copy=orders.copy ()
"""
Add "Fries" at the end.
Insert "Soup" at position 2.
Extend the list with ["Ice Cream", "Sandwich"].
Remove "Burger" (only the first one).
Pop the 3rd item and store it in a variable removed_order.
Count how many "Burger" remain.
Sort and reverse the list.
Make a copy of the final list into backup_orders.
Print everything clearly """
