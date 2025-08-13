available_balance = 1000
card_validity = True

while True:
    try:
        withdrawal_balance = int(input("Please enter the amount: "))
        
        if not card_validity:
            print("Invalid card. Please contact the bank.")
            break  # stop if card is invalid
        
        if withdrawal_balance > available_balance:
            print("Insufficient balance")
        
        elif withdrawal_balance % 100 != 0:
            print("Withdrawal amount must be in multiples of ₹100.")
        
        else:
            available_balance -= withdrawal_balance
            print(f"Withdrawal successful! New balance: ₹{available_balance}")
            break  # stop only if successful
    except ValueError:
        print("Please enter digits only.")
