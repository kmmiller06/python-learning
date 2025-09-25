"""
CS1300 - Homework 4: Decision Structures I
Name: Keegan Miller
Date: 9/24/2025
Description: Programs using conditional statements for decision-making
"""

#Problem 1
print("PROBLEM 1: Temperature Converter")
print("=" * 40)
print("=== Temperature Converter & Weather Advisor ===")
# Get temperature from user
temp = float(input("Enter temperature: "))
# Get the scale (C or F)
scale = input("Is this Celsius or Fahrenheit? (C/F): ").upper()
if scale == "C":
    fahrenheit = (temp * 9/5) + 32
    celsius = temp
elif scale == "F":
    celsius = (temp - 32) / 1.8
    fahrenheit = temp
print(f"Temperature (F): {fahrenheit} \nTemperature (C): {celsius}")
if fahrenheit < 32:
    print("Freezing! Bundle up warmly!")
elif fahrenheit <= 50:
    print("Cold - wear a warm jacket")
elif fahrenheit <= 70:
    print("Cool - a light jacket would be nice")
elif fahrenheit <= 85:
    print("Pleasant - enjoy the weather!")
elif fahrenheit > 85:
    print("Hot - stay hydrated")
# 1. Check which scale was entered
# 2. Convert to the other scale
# 3. Display both temperatures
# 4. Give weather advice based on Fahrenheit

#Problem 2
print("PROBLEM 2: Movie Theater Ticket System")
print("=" * 40)
print("=== Movie Theater Ticket System ===")
# Get customer information
age = int(input("Enter customer age: "))
day = input("Enter day of week: ").lower()
regular = 15
if day == "Tuesday":
    ticket = 7
    print(f"Your ticket price is {ticket}")
else:
    time = int(input("What time is the Movie? (24hr format): "))
    if age <= 12:
            ticket = 8
            print(f"Your ticket price is {ticket}")
    elif age >= 65:
        ticket = 10
        print(f"Your ticket price is {ticket}")
    elif time < 17:
        ticket = (regular - 3)
        print(f"Your ticket price is {ticket}")

# Remember:
# - Check for Tuesday special first
# - If not Tuesday, ask for show time
# - Apply age-based pricing
# - Apply matinee discount if applicable

#Problem 3
print("PROBLEM 3: Grade Calculator ")
print("=" * 40)
print("=== Grade Calculator ===")
# Get three test scores
test1 = float(input("Enter Test 1 score (0-100): "))
test2 = float(input("Enter Test 2 score (0-100): "))
test3 = float(input("Enter Test 3 score (0-100): "))
# YOUR CODE HERE
# 1. Validate all scores are between 0 and 100
# 2. If invalid, print error and stop
# 3. Calculate average
# 4. Determine letter grade using elif
# 5. Check passing criteria (D or better AND at least one test >= 60)
# 6. Display results

#Problem 4
print("PROBLEM 4: Password Strength Checker")
print("=" * 40)
print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")
# Initialize criteria counters
criteria_met = 0
feedback = []
# YOUR CODE HERE
# 1. Check each criterion
# 2. For each criterion met, increment criteria_met
# 3. For each criterion not met, add feedback message
# 4. Determine strength level
# 5. Display results and feedback
# Hint for checking digits:
has_digit = any(char.isdigit() for char in password)

#Problem 5
print("PROBLEM 5: Resuraunt Bill Calculator")
print("=" * 40)
print("=== Restaurant Bill Calculator ===")
# Get initial information
food_total = float(input("Enter food total: $"))
is_holiday = input("Is today a holiday? (yes/no): ").lower()
party_size = int(input("How many people in your party? "))
# YOUR CODE HERE
# Follow the requirements and calculation order
# Remember to ask additional questions based on conditions
# Display a detailed breakdown of the bill