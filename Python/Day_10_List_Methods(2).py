
# Create an initial grocery list
grocery_list = ["milk", "bread", "eggs"]

# 1. Add "butter" to the end of the list
grocery_list.append("butter")
print("After append:", grocery_list)

# 2. Insert "fruits" at index 1
grocery_list.insert(1, "fruits")
print("After insert at index 1:", grocery_list)

# 3. Remove the last item from the list using pop()
removed_item = grocery_list.pop(1)
print("Removed item:", removed_item)
print("After pop:", grocery_list)

# 4. Sort the list in alphabetical order
grocery_list.sort()
print("Sorted grocery list:", grocery_list)

# 5. Reverse the list
grocery_list.reverse()
print("Reversed grocery list:", grocery_list)
