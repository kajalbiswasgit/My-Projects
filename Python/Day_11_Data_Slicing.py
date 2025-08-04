# Just like slicing a cake, you're slicing a part of the list using this format:

"""
start: From where to start (0 means first)
stop: One step before where to stop (it will not include stop) 
# ### list[start:stop:step]
start: from where to begin (default = 0)
stop: where to stop (not included)
step: how many to skip (default = 1)

"""

# Example:1
colors = ["red", "green", "blue", "yellow", "purple"]
print(colors[0:3])  # From index 0 to index 2

# Example:2
print(colors[2:])  # From index 2 to end

# Example:3
print(colors[::2])  # Every second color
# Output: ['red', 'blue', 'purple']

# Example:3 (Reverse list)
print(colors[::-1])
# Output: ['purple', 'yellow', 'blue', 'green', 'red']

