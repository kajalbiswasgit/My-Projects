# Requirements:
"""Ask the user to enter:
Movie name
Number of tickets they want to book
Ticket price is ₹200 per ticket (fixed)
Input validations:
Number of tickets must be a number between 1 and 10 (max 10 tickets per booking).
Movie name must not be empty or numeric.
If inputs are valid:
Show total cost.
Ask: “Do you want to confirm booking? (yes/no)”
If yes: Show booking confirmed message.
If no: Show booking cancelled message."""

Movie_names = {"Marvel", "Spiderman", "Batman"}  # Set of available movie names
available_tickets = [10, 10, 10]  # Ticket availability per movie (order matters)
ticket_price = 200  # Fixed price per ticket

try:
    MovieName = input("Please enter the movie name (Marvel/Spiderman/Batman):")
    MovieName = MovieName.replace(" ", "").strip().title()

    if MovieName in Movie_names:
        print(f"{MovieName} is available. Proceeding with booking...")

        # Map movie name to its index in ticket list
        movie_index = list(Movie_names).index(MovieName)
        max_available = available_tickets[movie_index]

        try:
            No_of_tickets = input("How many tickets do you want? ").strip()
            if not No_of_tickets.isdigit():
                print("Please enter a valid number for tickets (1-10).")
            else:
                No_of_tickets = int(No_of_tickets)

                if No_of_tickets < 1 or No_of_tickets > 10:
                    print("You can book minimum 1 and maximum 10 tickets.")
                elif No_of_tickets > max_available:
                    print(f"Only {max_available} tickets are available for {MovieName}.")
                else:
                    total_cost = No_of_tickets * ticket_price
                    print(f"Total ticket price is: ₹{total_cost}")

                    while True:
                        confirmation = input("Do you want to confirm booking? (yes/no): ").lower().strip()
                        if confirmation == "yes":
                            print("Booking is confirmed.")
                            available_tickets[movie_index] -= No_of_tickets  # Reduce available tickets
                            break
                        elif confirmation == "no":
                            print("Booking is cancelled.")
                            break
                        else:
                            print("Please enter 'yes' or 'no' only.")
        except Exception as e:
            print("Something went wrong during ticket booking:", e)
    else:
        print("Invalid movie name. Please choose from the listed options.")
except Exception as e:
    print("Something went wrong:", e)
