# Menu items and prices
menu_items = ["Burger", "Sandwich", "French Fries"]  # Corrected spellings
price_list = [100, 115, 60]  # Prices for each item in the same order

print("--- Welcome to Hotel Akash ---")
print("Available items: " + ", ".join(menu_items))
customer_name = input("Enter your name: ").strip().title()
order_input = input("What do you want today? (Burger/Sandwich/French Fries): ").split(",")

order_list = []

for item in order_input:
    item = item.strip().lower()  
    if item == "fries":
        item = "French Fries"
    elif item == "burger":
        item = "Burger"
    elif item == "sandwich":
        item = "Sandwich"
    else:
        print(f"'{item}' is not in our menu!")
        continue
    order_list.append(item)

items_ordered = ", ".join(order_list)
bill_amount = 0
for item in order_list:
    if item in menu_items:  # Only if item exists in our menu
        index = menu_items.index(item)  # Find index in menu list
        bill_amount += price_list[index]  # Add corresponding price

# Print receipt
print("\n----- Receipt -----")
print("Customer Name: {}".format(customer_name))
print("Items Ordered: {}".format(items_ordered))
print("Total Amount: ₹{}".format(bill_amount))
print("-------------------")
