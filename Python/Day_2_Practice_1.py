pizza_order_status = "pending"

print("Pizza is", pizza_order_status)

treat = input("Have you ordered the pizza from Domino's? (yes/no): ")

if treat.lower() == "yes":
    pizza_order_status = "ordered"
elif treat.lower() == "no":
    pass
else:
 print ("Invalid input. Please enter only 'yes' or 'no'. ")

if pizza_order_status == "ordered":
    print("Payment of Poco M7 is successful")
else:
    print("Pizza is still pending. Waiting for the order.") 
