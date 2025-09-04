# lab3_1.py
# Week 3 Session 1 Lab
# Keegan Miller
# 9/4/25
print("=" * 50)
print("WEEK 3 SESSION 1 LAB")
print("=" * 50)

# Exercise 1
print("\n--- Exercise 1: Variable Memory Investigation ---")
# TODO: Create two variables with value 100 and check their memory
x = 100
y = 100
print(f"x = {x}, Memory ID: {id(x)}")
print(f"y = {y}, Memory ID: {id(y)}")
print(f"Same memory? {id(x) == id(y)}")
# TODO: Try with larger numbers (1000)
x1 = 1000
y1 = 1000
print(f"x = {x1}, Memory ID: {id(x1)}")
print(f"y = {y1}, Memory ID: {id(y1)}")
print(f"Same memory? {id(x1) == id(y1)}")
# TODO: Reassign x and check what happens to memory ID
original_id = id(x)
x = x + 50
new_id = id(x)
# Print comparison
# TODO: Change variable type and track memory
data = 42 # int
print(f"Data = {data}, Type: {type(data)} {id(data)}")
data = 3.14 # float
print(f"Data = {data}, Type: {type(data)} {id(data)}")
data = "Hello" # string
print(f"Data = {data}, Type: {type(data)} {id(data)}")

#Exercise 2
print("\n--- Exercise 2: Shopping Cart Calculator ---")
# Initialize cart
cart_total = 0.0
print(f"Starting total: ${cart_total:.2f}")
# TODO: Add 3 items using +=
item1 = float(input("Item 1 price: $"))
cart_total += item1
print(f"After item 1: ${cart_total:.2f}")
# Add item 2 (your code)
item2 = float(input("Item 2 price: $"))
cart_total += item2
print(f"After item 2: ${cart_total:.2f}")
# Add item 3 (your code)
item3 = float(input("Item 3 price: $"))
cart_total += item3
print(f"After item 3: ${cart_total:.2f}")
# TODO: Apply discount using -=
discount_percent = float(input("Discount %: "))
discount_amount = cart_total * (discount_percent / 100)
cart_total -= discount_amount
print(f"After {discount_percent}% discount: ${cart_total:.2f}")
# Subtract discount from total
# TODO: Add 8% tax using +=
tax_rate = 0.08
tax_amount = cart_total * tax_rate
cart_total = cart_total + tax_amount
# Calculate and add tax
print(f"Final Total: ${cart_total:.2f}")

# Exercise 3 
print("\n--- Exercise 3: Division Operations ---")
# Get two numbers
dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
# TODO: Calculate and display with types
regular_div = dividend / divisor
floor_div = dividend // divisor
modulo = dividend % divisor
print(f"{dividend} / {divisor} = {regular_div} (type: {type(regular_div).__name__})")
print(f"{dividend} // {divisor} = {floor_div} (type: {type(floor_div).__name__})")
print(f"{dividend} % {divisor} = {modulo} (type: {type(modulo).__name__})")
# TODO: Test float precision
a = 0.1
b = 0.2
c = a + b
print(f"\n{a} + {b} = {c}")
print(f"Is 0.1 + 0.2 == 0.3? {c == 0.3}")
# TODO: Test large integers
big = 10 ** 50
print(f"\n10^50 has {len(str(big))} digits")

#Exercise 4
print("\n--- Exercise 4: Time Converter ---")
total_seconds = int(input("Enter seconds: "))
# TODO: Calculate time components
days = total_seconds // 86400
remaining = total_seconds % 86400
hours = remaining // 3600
remaining = remaining % 3600
minutes = remaining // 60
seconds = remaining % 60
print(f"{total_seconds} seconds equals:")
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# Exercise 5
print("\n--- Exercise 5: Expression Evaluation ---")
# Predict each result BEFORE running!
# Expression 1
expr1 = 2 + 3 * 4 - 1
print(f"2 + 3 * 4 - 1 = {expr1}")
# What did you predict? 13
# Expression 2
expr2 = 10 / 2 + 3 * 4
print(f"10 / 2 + 3 * 4 = {expr2}")
# What did you predict? 17.0
# Expression 3
expr3 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {expr3}")
# What did you predict? 512
# TODO: Create your own complex expression
# Use at least 4 operators
my_expr = (4 + 3) / 2 * 2 
print(f"My expression result: {my_expr}")
# TODO: Show how parentheses change the result
no_parens = 10 + 20 * 30
with_parens = (10 + 20) * 30
print(f"Without parentheses: {no_parens}")
print(f"With parentheses: {with_parens}")

# Bonus Question
print("\n--- BONUS: Loan Calculator ---")
principal = float(input("Loan amount: $"))
annual_rate = float(input("Annual rate (%): "))
years = int(input("Years: "))
# Convert to monthly
monthly_rate = (annual_rate / 100) / 12
months = years * 12
# Calculate payment (formula provided)
if monthly_rate > 0:
    payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
else:
    payment = principal / months
print(f"Monthly payment: ${payment:.2f}")
