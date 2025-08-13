# Set the maximum allowed recharge amount
available_amount = 500

while True:
    try:
        # Ask user to enter the recharge amount
        recharge_amount = input("Please enter recharge amount: ")

        # Check if the input contains only digits (no letters or special characters)
        if not recharge_amount.isdigit():
            print("Amount must be digits only")  # Error message for invalid input
            continue  # Ask again

        # Convert the input string to an integer
        recharge_amount = int(recharge_amount)

        # Check if the amount is more than allowed limit (₹500)
        if recharge_amount > available_amount:
            print(f"Recharge amount must be ₹{available_amount} or less")
            continue  # Ask again

        # Check if amount is a multiple of 10
        if recharge_amount % 10 != 0:
            print("Recharge amount must be in multiples of ₹10")
            continue  # Ask again

        # Check if amount is positive
        if recharge_amount <= 0:
            print("Amount must be a positive number")
            continue  # Ask again

        # If all validations pass, perform recharge
        print(f"Recharge successful! Available balance is ₹{available_amount - recharge_amount}")
        break  # Exit the loop after successful recharge

    except ValueError:
        print("Amount must be a valid number")
