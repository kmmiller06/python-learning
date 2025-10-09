# Given this list:
inventory = ["pen", "pencil", "eraser", "ruler", "notebook"]
# Without using loops (not covered yet):
# 1. Print how many items are in inventory
print(len(inventory))
# 2. Check if "pencil" is in the list (print True/False)
print("pencil" in inventory)
# 3. Create a new list with the first and last items only
# Hint: Use len(), in operator, and indexing
new_list = [inventory[0], inventory[len(inventory) - 1]]

# For each variable, predict if it's mutable or immutable:
a = 42 # Mutable or Immutable? IMMUTABLE
b = "Python" # Mutable or Immutable? IMMUTABLE
c = [1, 2, 3] # Mutable or Immutable? MUTABLE
d = 3.14 # Mutable or Immutable? IMMUTABLE
e = True # Mutable or Immutable? IMMUTABLE
# Test your predictions by trying to change them

# Create these lists:
# 1. Use list() to convert the string "HELLO" to a list
hello_list = list("HELLO")
# 2. Create a list of five 7's using repetition
sevens = [7] * 5
# 3. Create a list mixing your name, age, and favorite color
name = "Keegan"
age = 20
favorite_color = "blue"
mixed_list = [name, age, favorite_color]
# 4. Create a 2x2 nested list representing a tic-tac-toe board
tic_tac_toe = [["X", "O", "X"],
                ["O", "X", "O"],
                ["X", "O", "X"]]

# Given these lists:
list1 = [10, 20, 30, 40, 50]
list2 = []
list3 = [100]
# Write code to:
# 1. Safely print the first element of each list (handle empty)
if list1:   
    print(list1[0])
if list2:
    print(list2[0])
if list3:
    print(list3[0])
# 2. Safely change the last element to 999 (if it exists)
if list2:
    list2[-1] = 999
# 3. Swap first and last elements of list1
list1[0], list1[-1] = list1[-1], list1[0]
# 4. Calculate the middle index of list1 and print that element
middle_index = len(list1) // 2
print(list1[middle_index])

# Create an empty list called 'colors'
colors = []
# Use append() to add:
# - "red" 
# - "blue"
# - "green"
# Print the list after each append
colors.append("red")
print(colors)
colors.append("blue")
print(colors)
colors.append("green")
print(colors)

# Start with this list:
numbers = [10, 30, 40]
# Use insert() to:
# 1. Add 20 between 10 and 30
numbers.insert(1, 20)
# 2. Add 5 at the beginning
numbers.insert(0, 5)
# 3. Add 50 at the end
numbers.append(50)
# Print after each insertion
print(numbers)
# Final result should be: [5, 10, 20, 30, 40, 50]

# Start with:
sorted_list = [15, 25, 35, 45]
# You need to add 30 to keep the list sorted
# 1. Find the correct position (without loops)
# 2. Use insert() to add 30 at that position
sorted_list.insert(2, 30)
# 3. Try adding 10 to the beginning
sorted_list.insert(0, 10)
# 4. Try adding 50 to the end
sorted_list.append(50)
# Keep list sorted throughout

# Start with:
fruits = ["apple", "banana"]
# Use extend() to add:
# - ["orange", "grape"]
# Print the result
fruits.extend(["orange", "grape"])
print(fruits)
# Now create a new list 'numbers' with [1, 2]
numbers = [1, 2]
# Use extend to add [3, 4, 5]
numbers.extend([3, 4, 5])
# Print the result
print(numbers)

# Predict the output, then test:
# Case 1:
list1 = [1, 2]
list1.append([3, 4])
# What is list1 now?
# Case 2:
list2 = [1, 2]
list2.extend([3, 4])
# What is list2 now?
# Case 3:
list3 = ['a']
list3.extend('bc')
# What is list3 now?

# You have three sources of data:
morning_temps = [65, 68, 70]
afternoon_temps = [75, 78]
evening_temps = [72, 70, 68]
# Create 'all_temps' list that combines all three
# Try three approaches:
# 1. Using extend() multiple times
all_temps = []
all_temps.extend(morning_temps)
all_temps.extend(afternoon_temps)
all_temps.extend(evening_temps)
# 2. Using + operator
# 3. Using += operator
# Which modified the original? Which created new lists?

# Start with:
animals = ["cat", "dog", "bird", "dog", "fish"]
# 1. Use remove() to remove "bird"
animals.remove("bird")
# 2. Use pop() to remove the last animal
animals.pop()
# 3. Use del to remove the first animal
del animals[0]
# Print after each operation
print(animals)

# Start with:
queue = ["Alice", "Bob", "Charlie", "David", "Eve"]
# Perform these operations:
# 1. David left the queue (remove by value)
queue.remove("David")
# 2. Serve the first person (remove and print who was served)
served_person = queue.pop(0)
print(served_person)
# 3. The last person gave up and left (just remove them)
queue.pop()
# Choose the appropriate method for each

# Given:
data = [10, 20, 30, 40, 50]
to_remove = 25 # Not in list!
# Write code to:
# 1. Safely try to remove 'to_remove' (check first)
# 2. Safely pop index 10 (check bounds first)
if len(data) > 10:
    data.pop(10)
# 3. Delete the middle element (calculate middle index)
middle_index = len(data) // 2
del data[middle_index]
# 4. Clear all but first and last elements using del with slice
del data[1:-1]

# Given:
colors = ["red", "blue", "green", "yellow"]
# Check and print whether:
# 1. "blue" is in the list
# 2. "purple" is in the list
# 3. "RED" is in the list (note the case!)
# 4. "black" is not in the list
print("blue" in colors)
print("purple" in colors)
print("RED" in colors)
print("black" not in colors)

# Given:
inventory = ["hammer", "nails", "screwdriver", "wrench"]
tool = "pliers"
# Write code to:
# 1. Check if tool is in inventory
# 2. If not, add it and print "Added [tool]"
# 3. If yes, print "[tool] already in inventory"
# Then try with tool = "hammer"
if tool not in inventory:
    inventory.append(tool)
    print(f"Added {tool}")
else:
    print(f"{tool} already in inventory")

tool = "hammer"
if tool not in inventory:
    inventory.append(tool)
    print(f"Added {tool}")
else:
    print(f"{tool} already in inventory")
    
