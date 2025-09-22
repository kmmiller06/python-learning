# CS 1300 - Homework 2
# Name: Keegan Miller
# Date: 9/18/25
# Description: Variables, Input/Output, and Type Conversions

#Problem 1
print("\n" + "=" * 40)
print("Problem 1: Personal Finance Calculator")
print("=" * 40)

income = float(input("Enter monthly income: "))
rent = float(input("Enter rent cost: "))
food = float(input("Enter food expenses: "))
transportation = float(input("Enter transportation cost: "))
other = float(input("Enter other expenses: "))
total = income + rent + food + transportation + other
balance = income - rent - food - transportation - other
savings_rate = balance / income 

print(f"{"=" * 40}")
print("Monthly Budget Report")
print(f"{"=" * 40}")
print(f"Income: ${income}")
print(f"{"-" * 40}")
print(f"Expenses: \n Housing: ${rent} \n Food: ${food} \n Transportation ${transportation} \n Other: ${other}")
print(f"{"-" * 40}")
print(f"Total expenses: ${total} \n Remaining Balance: ${balance} \n Savings Rate: {savings_rate}% ")
print(f"{"=" * 40}")

# Problem 2
print("\n" + "=" * 40)
print("Problem 2: Grade Statistics Calculator")
print("=" * 40)
print("*" * 40)
print("Grade statistics calculator")
print("*" * 40)

test1 = float(input("Enter your score for test 1 (out of 100): "))
test2 = float(input("Enter your score for test 2 (out of 100): "))
test3 = float(input("Enter your score for test 3 (out of 100): "))
test4 = float(input("Enter your score for test 4 (out of 100): "))
test5 = float(input("Enter your score for test 5 (out of 100): "))
total = (test1 + test2 + test3 + test4 + test5)
average = (total / 5)
pointsfor90 = (450 - total)
print("*" * 40)
print("Grade Report)")
print("*" * 40)
print(f"Test 1: {test1}/100")
print(f"Test 2: {test2}/100")
print(f"Test 3: {test3}/100")
print(f"Test 4: {test4}/100")
print(f"Test 5: {test5}/100")
print("*" * 40)
print(f"Statistics: \n Total Points: {total:.2f}/500 \n Average Score: {average:.2f} \n Overall Grade: {average:.2f}% \n Points needed for 90%: {pointsfor90:.2f}")

# ============ Problem 3: Time Zone Converter ============
print("\n" + "=" * 40)
print("Problem 3: Time Zone Converter")
print("=" * 40)
hour = int(input("Enter the current hour (0-23): "))
minute = int(input("Enter the current minute (0-59): "))
time_zones = {
    "EST": 0,
    "CST": -1,
    "MST": -2,
    "PST": -3
}
print("+--------------------------------------+")
print("|             CURRENT TIMES             |")
print("+--------------------------------------+")
print("| Time Zone |   Time   |  12-hr Format |")
print("|-----------|----------|---------------|")

# Calculate and display times
for zone, offset in time_zones.items():
    new_hour = (hour + offset) % 24
    time_24 = f"{new_hour:02d}:{minute:02d}"
    time_12 = to_12_hour(new_hour, minute)
    print(f"| {zone:<9} | {time_24:<8} | {time_12:<13} |")

print("+--------------------------------------+")
# ============ Problem 4: Recipe Scaler ============
print("\n" + "=" * 40)
print("Problem 4: Recipe Scaler")
print("=" * 40)
print("\n" + "#" * 48)
print("RECIPE SCALER")
print("#" * 48)

# Get serving sizes
original_servings = int(input("Enter original serving size: "))
desired_servings = int(input("Enter desired serving size: "))

# Scaling factor
factor = desired_servings / original_servings

# Get ingredients
print("Enter 5 ingredients:")
ingredients = []
for i in range(1, 6):
    name = input(f"Ingredient {i} name: ")
    amount = float(input("Amount: "))
    unit = input("Unit: ")
    ingredients.append((name, amount, unit))

# Results
print("\n" + "#" * 48)
print("RECIPE SCALING RESULTS")
print("#" * 48)
print(f"Scaling factor: {factor:.2f}x ({original_servings} → {desired_servings} servings)")

print("-" * 48)
print(f"{'Original Recipe ('+str(original_servings)+' servings)'} | {'Scaled Recipe ('+str(desired_servings)+' servings)'}")
print("-" * 29 + "|" + "-" * 27)

# Display ingredients side by side
for name, amount, unit in ingredients:
    scaled = amount * factor
    print(f"{name}: {amount:5.2f} {unit:<6} | {name}: {scaled:5.2f} {unit:<6}")
print("\n" + "=" * 50)
print("END OF HOMEWORK 2")
print("=" * 50)


