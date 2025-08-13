#| Line No.   | Code                            | Explanation                                                                                                                                                                                                                                                                        |
""" | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
1 | `# List of 3 tools you are learning`        | ✅  This is just a note for humans. Python ignores this. Anything after `#` is a comment.                                                                                                                                                                              |
2 | `tools = ["Selenium", "Postman", "Git"]`    | ✅ **List creation** – You are creating a list named `tools`. It contains 3 string values: `"Selenium"`, `"Postman"`, and `"Git"`.
                                                      You can access each tool using its **index** (position).                                                                     |
3 | `for i in range(len(tools)):`               | ✅  🔹 `len(tools)` counts how many items are in the list → here it returns `3`.
                                                     🔹 `range(3)` gives numbers from 0 to 2 → `[0, 1, 2]`.
                                                     🔹 `for i in ...` means: Do this block **3 times**, once for each number `i` (0, 1, 2). |
4 | `print(f"{i+1}. I am learning {tools[i]}")` | ✅ Formatted print** using `f-string`.
                                                    🔹 `i+1` is used to show the count starting from 1 instead of 0.
                                                    🔹 `tools[i]` fetches the item from the list based on index `i`. 
                                                    🔹 It prints the message with numbering like: `1. I am learning Selenium`|"""

#Practice-
# List of favorite websites
# Print each website with its number using the same logic

websites = ["YouTube", "Google", "GitHub", "StackOverflow"]
for i in range(len(websites)):
    print (f"{i+1}. its a wesbsite {websites[i]}")


