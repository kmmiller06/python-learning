"""
CS1300 - Homework #5: Advanced Control Structures
Name: Keegan Miller
Date: 10/6/25
Description: Advanced conditional logic and validation
"""
# Problem 1
print("=== SMART THERMOSTAT SYSTEM ===")
# Get inputs
current_temp = float(input("Current temperature (F): "))
desired_temp = float(input("Desired temperature (F): "))
hour = int(input("Current hour (0-23): "))
season = input("Season (summer/winter/spring/fall): ").lower()
# YOUR CODE HERE
# 1. Check if current temp is in comfortable range using chained comparisons
if 68 <= current_temp <= 76:
    print("Current temperature is comfortable.")
# 2. Determine if it's night time (22-6)
if hour >= 22 or hour <= 6:
    print("It's night time. Adjusting temperature for energy savings.")
# 3. Apply seasonal restrictions
if season == "summer" and desired_temp < 68:
    desired_temp = 68
    print("Summer mode: Minimum temperature set to 68F.")
elif season == "winter" and desired_temp > 78:
    desired_temp = 78
    print("Winter mode: Maximum temperature set to 78F.")
# 4. Calculate actual target temperature after adjustments
# 5. Calculate time to reach target
# 6. Determine energy efficiency (Excellent/Good/Fair/Poor) based on adjustments
# Hint: Use chained comparisons like: 68 <= current_temp <= 76
# Hint: Night check needs: hour >= 22 or hour <= 6

#Problem 2
print("=== PASSWORD SECURITY ANALYZER ===")
password = input("Enter password to analyze: ")
# Initialize score
score = 0
# YOUR CODE HERE
# Use conditional expressions for each check
# Example: length_points = 30 if len(password) >= 16 else 20 if len(password) >=12 else 10 if len(password) >= 8 else 0
# Check length (use conditional expression)
length_points = 30 if len(password) >= 16 else 20 if len(password) >=12 else 10 if len(password) >= 8 else 0
# Check for uppercase (use conditional expression)
has_upper = password != password.lower()
upper_points = 10 if has_upper else 0
# Check for lowercase
has_lower = password != password.upper() and any(c.islower() for c in password)
lower_points = 10 if has_lower else 0
# Check for numbers
has_digit = any(c.isdigit() for c in password)
digit_points = 10 if has_digit else 0
# Check for special characters
has_special = not password.isalnum()
special_points = 10 if has_special else 0
# Check for common patterns
common_patterns = ["123", "abc", "qwerty", "password", "111"]
has_pattern = any(pattern in password.lower() for pattern in common_patterns)
pattern_points = 0 if has_pattern else 20
# Calculate total score and determine strength level
# Display detailed analysis

#Problem 3
print("=== GRADE VALIDATION SYSTEM ===")
# Get four test scores
test1 = float(input("Test 1 score: "))
test2 = float(input("Test 2 score: "))
test3 = float(input("Test 3 score: "))
test4 = float(input("Test 4 score: "))
# YOUR CODE HERE
# 1. Validate each score is 0-100 using chained comparisons
# 2. Check for suspicious patterns
# 3. Use truth table logic:
# valid_range AND not_suspicious AND not_identical
# 4. If valid, calculate average, highest, lowest, improvement
# 5. Provide appropriate feedback
# Example validation:
all_valid_range = (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100) and (0 <= test4 <= 100)
# Check if all identical
all_identical = (test1 == test2 == test3 == test4)
# Check for huge jumps
huge_jump = (abs(test2 - test1) > 20) or (abs(test3 - test2) > 20) or (abs(test4 - test3) > 20)
# Combine validations using truth table logic
valid_scores = all_valid_range and not all_identical and not huge_jump
if valid_scores:
    average_score = (test1 + test2 + test3 + test4) / 4
    highest_score = max(test1, test2, test3, test4)
    lowest_score = min(test1, test2, test3, test4)
    improvement = test4 - test1
    print(f"Average: {average_score}, Highest: {highest_score}, Lowest: {lowest_score}, Improvement: {improvement}")
else:
    print("Invalid or suspicious score patterns detected.")
    
#Problem 4
print("=== EVENT SCHEDULING SYSTEM ===")
# Event 1
print("\nEVENT 1 DETAILS:")
event1_name = input("Event name: ")
event1_day = input("Day (Mon-Sun): ").lower()[:3] # First 3 letters
event1_start = float(input("Start time (0-24): "))
event1_end = float(input("End time (0-24): "))
# Event 2
print("\nEVENT 2 DETAILS:")
event2_name = input("Event name: ")
event2_day = input("Day (Mon-Sun): ").lower()[:3]
event2_start = float(input("Start time (0-24): "))
event2_end = float(input("End time (0-24): "))
# YOUR CODE HERE
# 1. Validate times are in range 0-24
# 2. Validate end time > start time for each event
# 3. Check for conflicts using complex conditions
# 4. Calculate gap between events if same day
# 5. Check for early/late scheduling issues
# Valid days
valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
# Validation using chained comparisons
event1_valid = (event1_day in valid_days) and (0 <= event1_start < 24) and (0 < event1_end <= 24) and (event1_end > event1_start)
event2_valid = (event2_day in valid_days) and (0 <= event2_start < 24) and (0 < event2_end <= 24) and (event2_end > event2_start)
# Check for conflicts
same_day = event1_day == event2_day
overlap = not (event1_end <= event2_start or event2_end <= event1_start)
if same_day and overlap:
    print("Conflict detected between events.")
    
#Problem 5
print("=== RETAIL DISCOUNT CALCULATOR ===")
# Get inputs
price = float(input("Item price: $"))
quantity = int(input("Quantity: "))
customer_type = input("Customer type (regular/member/vip/employee): ").lower()
day = input("Day of week: ").lower()
coupon = input("Coupon code (or 'none'): ").upper()
# YOUR CODE HERE
# Calculate each discount using conditional expressions
# Apply discounts in order (multiplicative, not additive)
# Check maximum discount rule
# Show complete breakdown
# Calculate subtotal
subtotal = price * quantity
# Bulk discount (use conditional expression)
bulk_rate = 0.10 if quantity >= 20 else 0.05 if quantity >= 10 else 0
bulk_discount = subtotal * bulk_rate
subtotal_after_bulk = subtotal - bulk_discount
# Customer type discount    
customer_discount_rate = 0.05 if customer_type == "member" else 0.10 if customer_type == "vip" else 0.20 if customer_type == "employee" else 0
customer_discount = subtotal_after_bulk * customer_discount_rate
subtotal_after_customer = subtotal_after_bulk - customer_discount
# Day-based discount
day_discount_rate = 0.10 if day == "tuesday" else 0.05 if day == "thursday" else 0
day_discount = subtotal_after_customer * day_discount_rate
subtotal_after_day = subtotal_after_customer - day_discount
# Coupon discount
coupon_discount_rate = 0.15 if coupon == "BLACKFRIDAY" else 0.10 if coupon == "CYBERMONDAY" else 0
coupon_discount = subtotal_after_day * coupon_discount_rate
total = subtotal_after_day - coupon_discount
# Display breakdown
print(f"Subtotal: ${subtotal:.2f}")
print(f"Bulk discount: -${bulk_discount:.2f}")
print(f"Customer discount: -${customer_discount:.2f}")
print(f"Day discount: -${day_discount:.2f}")
print(f"Coupon discount: -${coupon_discount:.2f}")
print(f"Total: ${total:.2f}")