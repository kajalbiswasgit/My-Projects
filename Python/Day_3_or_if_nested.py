#✅ 1. or – Either condition is True
#🔸 Meaning:
#If any one of the conditions is True, the whole condition is True.

"""🔸 Syntax: """

# if condition1 or condition2:

### Example 
day = input("What is today: ").strip().lower()
# First, check for invalid number input
if any(char.isdigit() for char in day):
    print("❌ Numbers are not allowed. Please enter a valid day.")
elif day == "saturday" or day == "sunday":
    print("✅ It's a weekend!")
else:
    print("It's a weekday.")
