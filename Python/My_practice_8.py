inventory = ["Rice", "Sugar", "Salt", "Oil", "Soap", "Shampoo", "Biscuits", "Flour", "Milk"]
print (inventory[0])
print (inventory [6:9])
print (inventory [1::2])
inventory.append ("Tea")
inventory.append("Coffee")
inventory.append("Noodles")
print (inventory)
inventory.remove ("Salt")
inventory.remove ("Oil")
inventory.remove ("Soap")
inventory.insert (3,"Detergent")
inventory.insert (2,"Mustard Oil")
final_inventory=inventory

print (inventory)
final_inventory.sort()
print ("Total items:",len(inventory))
if "Tea" in inventory:
    print ("Tea is avaialable")
else:
    print ("Tea is not available")
final_inventory.pop()
final_inventory.sort()
print (final_inventory)
#Perform these steps in order:

"""Print the first item in the list.
Print the last three items in the list.
Print every second item starting from "Sugar".
Add "Tea", "Coffee", and "Noodles" to the list.
Remove "Salt" and "Oil".
Replace "Soap" with "Detergent".
Insert "Mustard Oil" right after "Sugar".
Print the final inventory in one line."""