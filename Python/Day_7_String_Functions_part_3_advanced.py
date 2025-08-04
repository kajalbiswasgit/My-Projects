#| 🔤 Method      | 📋 Description                              | 🧪 Example                               |
"""| -------------- | ------------------------------------------- | ---------------------------------------- |
| `lower()`      | Converts all characters to lowercase        | `"Python".lower()` → `"python"`          |
| `upper()`      | Converts to uppercase                       | `"python".upper()` → `"PYTHON"`          |
| `strip()`      | Removes leading/trailing spaces             | `"  hello ".strip()` → `"hello"`         |
| `replace()`    | Replaces part of the string                 | `"a-b-c".replace("-", "")` → `"abc"`     |
| `startswith()` | Checks if string starts with a value        | `"testcase".startswith("test")` → `True` |
| `endswith()`   | Checks if string ends with a value          | `"file.txt".endswith(".txt")` → `True`   |
| `isdigit()`    | Checks if all characters are digits         | `"1234".isdigit()` → `True`              |
| `isalpha()`    | Checks if all characters are letters        | `"abc".isalpha()` → `True`               |
| `isalnum()`    | Checks if all characters are letters/digits | `"abc123".isalnum()` → `True`            |
| `find()`       | Finds position of a substring               | `"email@test.com".find("@")` → `5`       |
| `split()`      | Splits string into a list                   | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
| `join()`       | Joins list items into a string              | `"".join(['a','b'])` → `"ab"`            |"""

#Practice Task (Today)
"""Write a program that:
Takes a full name input from user
Removes any extra spaces
Converts name to proper case (e.g., Kajal Biswas)
Splits first and last name
Prints welcome message"""

name = input("Enter your full name: ").strip()

# Clean up and format the name
name = " ".join(name.split())  # remove multiple internal spaces
name = name.title()  # make first letters capital

# Split first and last name
parts = name.split(" ")

if len(parts) >= 2:
    first_name = parts[0]
    last_name = parts[1]
    print(f"Welcome {first_name} {last_name}!")
else:
    print("Please enter both first and last name.")
