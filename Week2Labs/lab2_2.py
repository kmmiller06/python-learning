# lab2_2.py
# Week 2 Session 2 Lab
# Keegan Miller
# 8/28/25
print("=" * 50)
print("WEEK 2 SESSION 2 LAB - INPUT/OUTPUT PRACTICE")
print("=" * 50)

# ==================== PART 1: TYPE CONVERSION ====================

# Problem 1: Age Calculator
print("\n--- Problem 1: Age Calculator ---")
# TODO: Get birth year from user and convert to integer
birth_year = int(input("Enter your Birth Year:"))
# TODO: Calculate age (assume current year is 2024)
current_year = 2024
age = current_year - birth_year 
# TODO: Print "You are ___ years old in 2024."
print(f"You are {age} years old in 2024.")
# Test with: 2000 → Should output: You are 24 years old in 2024.

# Problem 2: Temperature Converter
print("\n--- Problem 2: Temperature Converter ---")
# TODO: Get Celsius temperature and convert to float
cels_temp = float(input("What is the current Temperature in Celsius?:"))
# TODO: Calculate Fahrenheit
faren_temp = (cels_temp * 9/5) + 32
# TODO: Print both temperatures with 1 decimal place
print(f"{cels_temp:.1f}°C = {faren_temp:.1f}°F")
# Test with: 25 → Should output: 25.0°C = 77.0°F

#Problem 3: Rectangle Measurements
print("\n--- Problem 3: Rectangle Measurements ---")
# TODO: Get length and width as floats
length = float(input("What is the length?:"))
width = float(input("What is the width?:"))
# TODO: Calculate area and perimeter
area = length * width
perimeter = (length * 2) + (width * 2)

# TODO: Display with 2 decimal places
print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")
# Test with: length=5.5, width=3.2
# Should output: Area: 17.60, Perimeter: 17.40

# Problem 4: Bill Calculator
print("\n--- Problem 4: Bill Calculator ---")
# TODO: Get meal cost and tip percentage
cost = float(input("How much did your meal cost?: $"))
tip_input = input("What percent tip would you like to leave?:")
tip_input = tip_input.replace("%", "")
tip_percent = float(tip_input)
# TODO: Calculate tip amount and total
tip = cost * (tip_percent / 100)
total = cost + tip
# TODO: Display all amounts with 2 decimal places
print(f"Meal: ${cost:.2f}")
print(f"Tip: ${tip:.2f}") 
print(f"Total: ${total:.2f}")
# Test with: meal=$50, tip=20%
# Should output: Meal: $50.00, Tip: $10.00, Total: $60.00

# ==================== PART 2: PRINT FUNCTION ====================

# Problem 5: Student Info Display
print("\n--- Problem 5: Student Info Display ---")
# TODO: Get name, age, major from user
name = input("What is your name?: ")
age = input("What is your age?: ")
major = input("What is your major?: ")
# TODO: Display with:
# 1. Default spacing
print(name, age, major)
# 2. Comma separation (use sep=", ")
print(name, age, major, sep=", ")
# 3. Pipe separation (use sep=" | ")
print(name, age, major, sep=" | ")
# Test with: Alice, 20, Computer Science
# Should show three different formats

# Problem 6: Progress Indicator
print("\n--- Problem 6: Progress Indicator ---")
# TODO: Print "Processing" without newline
print("Processing", end="")
# TODO: Add 5 dots without newlines (use end="")
print(".....", end="")
# TODO: Print " Complete!"
print("Complete!")
# Should output: Processing..... Complete!

# Problem 7: Data Table Header
print("\n--- Problem 7: Data Table Header ---")
# TODO: Print a line of 40 equal signs
print("=" * 40)
# TODO: Print "Name", "Score", "Grade" with tab separation
print("Name", "Score", "Grade", sep= "\t")
# TODO: Print another line of 40 equal signs
print("=" * 40)
# TODO: Get and display one student's data with tabs
name = input("Enter student's name: ")
score = input("Enter student's score: ")
grade = input("Enter student's grade: ")
print(name, score, grade, sep="\t")
# Should create a simple table structure

# Problem 8: Message Box
print("\n--- Problem 8: Message Box ---")
# TODO: Get a short message from user
message = input("What is your message?: ")
# TODO: Print top border (use "+" and "-" × 30)
print("+" + "-" * 30 + "+")
# TODO: Print message with "| " before and after
print("| " + message.center(28) + " |")
# TODO: Print bottom border
print("+" + "-" * 30 + "+")
# Test with: "Hello World"
# Should create a box around the message

# ==================== PART 3: F-STRING FORMATTING ====================

# Problem 9: Price Display
print("\n--- Problem 9: Price Display ---")
# TODO: Get item name and price
item_name = input("What is the item name?: ")
price = float(input("What is the item price?: "))
# TODO: Display as: "Item: ________ Price: $__.__ "
print(f"Item: {item_name} Price: ${price:.2f}")
# TODO: Use f-string to right-align price in 8 characters
print(f"{item_name:<10} ${price:8.2f}")
# Test with: Apple, 1.5
# Should output: Apple $ 1.50

# Problem 10: Percentage Calculator
print("\n--- Problem 10: Percentage Calculator ---")
# TODO: Get earned points and total points
earned = float(input("Enter earned points: "))
total = float(input("Enter total points: "))
# TODO: Calculate percentage
percentage = (earned / total) * 100
# TODO: Display as: "Score: __/__ = __%"
print(f"Score:{earned:.0f}/{total:.0f} = {percentage:.1f}%")
# TODO: Show percentage with 1 decimal place
# Test with: 85 out of 100
# Should output: Score: 85/100 = 85.0%

# Problem 11: Receipt Line Item
print("\n--- Problem 11: Receipt Line Item ---")
# TODO: Get product, quantity, unit price
product = input("Enter the product: ")
quantity = int(input("Enter the quantity: "))
unit_price = float(input("Enter the unit price: $"))
# TODO: Calculate total price
total_price = (unit_price * quantity)
# TODO: Display with:
# - Product left-aligned (20 chars)
print(f"{product:<20}{quantity:^10}${total_price:>10.2f}")
# - Quantity centered (10 chars)
# - Total right-aligned with $ (10 chars)
# Test with: Notebook, 3, 2.50
# Output: Notebook 3 $ 7.50

#Problem 12: ID Formatter
print("\n--- Problem 12: ID Formatter ---")
# TODO: Get a number from user
user_number = int(input("Enter a number: "))
# TODO: Display as:
# - 4-digit ID
# - 6-digit ID
# - 8-digit ID
print(f"4-digit: {user_number:04d}")
print(f"6-digit: {user_number:06d}")
print(f"8-digit: {user_number:08d}")
# TODO: All with leading zeros
# Test with: 42
# Should output:
# 4-digit: 0042
# 6-digit: 000042
# 8-digit: 00000042

print("\n" + "=" * 50)
print("LAB COMPLETED!")
print("=" * 50)

