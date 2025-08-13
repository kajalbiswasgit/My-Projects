#Requirements:
"""Ask the user to enter the total bill amount.
If the bill is:
More than ₹1000 → give 10% discount
Between ₹500 and ₹1000 → give 5% discount
Less than ₹500 → no discount
Validate that the bill amount is a positive number and not alphabetic.
Show final payable amount."""

try:
    total_bill= input ("please enter your total bill:").strip()
    if not total_bill.replace(",","",1).isdigit():
        print ("Bill amount must be in digits only")
    else:
        total_bill=float(total_bill)
        if total_bill <= 0:
            print("Bill amount must be positive.")
        else:
            if total_bill > 1000:
                discount= total_bill * 0.10
            elif total_bill >= 500:
                discount = total_bill * 0.05
            else:
                discount=0
            
            final_amount= total_bill - discount
            print (f"Discount applied:{discount:.2f}")
            print (f"total amount needs to be paid:{final_amount:.2f}")
except Exception as e:
    print ("something went wrong",e)

            


