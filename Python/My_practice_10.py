# You are managing an orders list for a clothing store.

"""Create a list of the following initial orders:
"T-Shirt", "Jeans", "Jacket", "T-Shirt", "Shoes"
A customer just ordered "Cap". Add it to the end of the list.
Another customer placed an order for "Socks", but they want it to be in second position in the list. Insert it accordingly.
Add multiple new items in one go: "Belt", "Scarf", "Sweater".
A "T-Shirt" order got canceled — remove only the first occurrence.
Another order at the third position was also canceled — remove it and store it in a variable called removed_item.
Count how many "T-Shirt" orders remain.
Sort the list alphabetically, then reverse it so it’s in descending order.
Make a backup copy of the current list."""

recent_orders= ["T-Shirt", "Jeans", "Jacket", "T-Shirt", "Shoes"]
recent_orders.append ("Cap")
recent_orders.insert (1,"Socks")
recent_orders.extend (["Belt", "Scarf", "Sweater"])
recent_orders.pop(recent_orders.index("T-Shirt"))
removed_item= recent_orders.pop(3)
print ("Removed item:",removed_item)
print ("T-shirt left:",recent_orders.count("T-Shirt"))
recent_orders.sort()
recent_orders.reverse()
copy=recent_orders.copy()
print (recent_orders)


