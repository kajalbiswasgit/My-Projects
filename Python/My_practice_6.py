#Task Name: 🚌 Bus Ticket Booking System
"""
Show the user a list of available bus routes.
Ask the passenger to enter the route they want, but allow them to type in short forms
(e.g., "kol-del" should be converted to "Kolkata to Delhi").
Ask for passenger names (multiple names separated by commas).
Clean the input by removing extra spaces and capitalizing names properly.
Use join() to display passenger names in one line.
Use format() to print a ticket receipt."""

bus_routes=["Kolkata to Delhi","Delhi to Kolkata"]
ticket_price= 900
print ("___welcome to kajal bus services___")
print ("Available buses are: "+ ", ".join (bus_routes))
bus_name= input ("which route bus do you want?(Kolkata to Delhi or Delhi to Kolkata):").strip ().lower ()
if bus_name == "kol to del":
        bus_name = "Kolkata to Delhi"
elif bus_name == "del to kol":
        bus_name = "Delhi to Kolkata"
else:
        print ("Route Not available")
        exit()
raw_names = input("Enter passenger names (comma separated): ").split(",")
passenger_names = [name.strip().title() for name in raw_names]

ticket_count= (input ("how many tickets do you want?:"))
if not ticket_count.isdigit():
    print ("Ticket count should be in digits only.")
    exit ()

ticket_count = int(ticket_count)

bill_amount= ticket_price * ticket_count

print ("Total amount is:",bill_amount)
print("\n----- Ticket Receipt -----")
print("Route: {}".format(bus_name))
print("Passengers: {}".format(", ".join(passenger_names)))
print("Total Tickets: {}".format(ticket_count))
print("Total Price: ₹{}".format(bill_amount))
print("--------------------------")
