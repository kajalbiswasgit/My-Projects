"""| **Concept**  | **Simple Explanation**                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------- |
| `for` loop   | Repeats code a fixed number of times. Example: Count 1 to 10.                                       |
| `while` loop | Repeats code until a condition becomes false**. Example: Keep asking until user enters correct input. |
| `range()`    | Gives a list of numbers to use in `for` loop. Example: `range(1, 6)` gives 1 to 5.                      |
| `break`      | Stops the loop immediately. Useful when condition is met early.                                     |
| `continue`   | Skips the **current round** and jumps to the next. Example: Skip printing number 13.                    |
"""

# for loop----
# “I want to print numbers 1 to 5”

for i in range(1,6): #range(1, 6)” means 1 to 5 (not including 6)
    print (i)

#  while loop---
#  “Keep asking the user to enter a number until they enter a valid one (1 to 10)”

while True:
    number = input("Enter a number between 1 and 10: ")
    if number == "7":
        print("Correct!")
        break
    else:
        print("Try again, correct no is 7")


# break--
# “Stop the loop now”

for i in range(1, 10):
    if i == 4:
        break
    print(i)  #It prints 1 to 3 only. When it reaches 4, it stops the loop.


# continue--
# “Skip this step and go to the next one”

for i in range(1, 6):
    if i == 3:
        continue
    print("value of i is:", i)

