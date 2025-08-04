#| Function                    | Description                                  |
"""|--------------------------- | -------------------------------------------- |
| `dict[key]`                 | Access the value of the given key            |
| `dict[key] = value`         | Update the value or add a new key-value pair |
| `del dict[key]`             | Delete a specific key-value pair             |
| `dict.get(key)`             | Returns value if key exists, else `None`     |
| `dict.keys()`               | Returns a list of all keys                   |
| `dict.values()`             | Returns a list of all values                 |
| `dict.items()`              | Returns a list of (key, value) tuples        |
| `dict.update({key: value})` | Adds or updates multiple items               |
| `len(dict)`                 | Returns the number of items                  |
| `key in dict`               | Check if a key exists in dictionary          |"""
details= {"name:":"kajal", "Roll:":39}
print ("Student details:",details["name:"])
print ("Student roll:",details["Roll:"])
details ["Age:"]= 28 # add value
details ["Marks:"]= 57 # add value
details ["Roll:"]=40 # Change value
del details ["Age:"]  # delete value



# Display All
print("Updated student:", details)
print("Keys:", details.keys())
print("Values:", details.values())
print("Items:", details.items())

