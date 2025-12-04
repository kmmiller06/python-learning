"""
CS1300 - Homework #5: Advanced Control Structures
Name: Keegan
Date: 10/6/25
Description: Advanced conditional logic and validation
"""

#Problem 1
print("=== SMART THERMOSTAT SYSTEM ===")
# Get inputs
current_temp = float(input("Current temperature (F): "))
desired_temp = float(input("Desired temperature (F): "))
hour = int(input("Current hour (0-23): "))
season = input("Season (summer/winter/spring/fall): ").lower()
# YOUR CODE HERE
print("Current Status:")
# 1. Check if current temp is in comfortable range using chained comparison
if 68 <= current_temp <= 76:
    print(f"Current Temp: {current_temp}F (Comfortable)")
else:
    print(f"Current Temp: {current_temp}F (Uncomfortable)")
# 2. Determine if it's night time (22-6)
night = (hour >= 22) or (hour <= 6)
print(f"- Night mode: {night}")
# 3. Apply seasonal restrictions
if season == "winter":
    max_allowed = 70
elif season == "summer":
    max_allowed = 78
else:
    max_allowed = 75  # spring/fall
print(f"- Seasonal max allowed: {max_allowed}F")
# 4. Calculate actual target temperature after adjustments
target = desired_temp
if night:
    target -= 3
    
if target > max_allowed:
    target = max_allowed
print(f" - Final target temperature: {target}F")
# 5. Calculate time to reach target
difference = target - current_temp
if difference > 0:
    time_to_target = difference / 2  
else: 
    time_to_target = 0
print(f"- Estimated time to reach target: {time_to_target:.1f} hours")
# 6. Determine energy efficiency (Excellent/Good/Fair/Poor)
if difference <= 2:
    efficiency = "Excellent"
elif difference <= 5:
    efficiency = "Good"
elif difference <= 10:
    efficiency = "Fair"
else:
    efficiency = "Poor"

print(f"Energy efficiency: {efficiency}")
# Hint: Use chained comparisons like: 68 <= current_temp <= 76
# Hint: Night check needs: hour >= 22 or hour <= 6

#Problem 2
print("=== PASSWORD SECURITY ANALYZER ===")
password = input("Enter password to analyze: ")
# Initialize score
score = 0
# YOUR CODE HERE
# Use conditional expressions for each check
# Check length (use conditional expression)
length_points = 30 if len(password) >= 16 else 20 if len(password) >= 12 else 10 if len(password) >= 8 else 0
# Check for uppercase (use conditional expression)
has_upper = password != password.lower()
upper_points = 20 if has_upper else 0
# Check for lowercase
has_lower = password != password.upper()
lower_points = 20 if has_lower else 0
# Check for numbers
has_digit = any(c.isdigit() for c in password)
digit_points = 20 if has_digit else 0
# Check for special characters
has_special = not password.isalnum()
special_points = 20 if has_special else 0
# Check for common patterns
common_patterns = ["123", "abc", "qwerty", "password", "111"]
has_pattern = any(pattern in password.lower() for pattern in common_patterns)
pattern_points = 0 if has_pattern else 20
# Calculate total score and determine strength level
score = (length_points + upper_points + lower_points + digit_points + special_points + pattern_points)
if score >= 90:
    strength = "Very Strong"   
elif score >= 75:
    strength = "Strong"
elif score >= 50:
    strength = "Good"
else:
    strength = "Weak"
# Display detailed analysis

#Problem 3
print("=== GRADE VALIDATION SYSTEM ===")

# Get four test scores
test1 = float(input("Test 1 score: "))
test2 = float(input("Test 2 score: "))
test3 = float(input("Test 3 score: "))
test4 = float(input("Test 4 score: "))

# 1. Validate each score is 0-100 using chained comparisons
all_valid_range = (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100) and (0 <= test4 <= 100)

# 2. Check for suspicious patterns
all_identical = (test1 == test2 and test2 == test3 and test3 == test4)
all_perfect = (test1 == 100 and test2 == 100 and test3 == 100 and test4 == 100)

jump1 = abs(test2 - test1)
jump2 = abs(test3 - test2)
jump3 = abs(test4 - test3)
huge_jump = (jump1 > 40 or jump2 > 40 or jump3 > 40)

any_suspicious = all_identical or all_perfect or huge_jump

# 3. Truth table logic:
# valid_range AND not_suspicious AND not_identical
record_is_valid = all_valid_range and not any_suspicious

print("\nValidation Results:")

if all_valid_range:
    print("All scores are in the valid range")
else:
    print("At least one score is outside 0-100")

if all_identical:
    print("All four scores are identical")
if huge_jump:
    print("There are large jumps between test scores")
if all_perfect:
    print("All test scores are perfect")
if not any_suspicious and all_valid_range:
    print("Scores show normal variation")

# 4. If valid, calculate average, highest, lowest, improvement
if record_is_valid:
    scores = [test1, test2, test3, test4]
    average = (test1 + test2 + test3 + test4) / 4
    highest = max(scores)
    lowest = min(scores)
    improvement = test4 - test1

    if improvement > 0:
        trend = "IMPROVING"
    elif improvement < 0:
        trend = "DECLINING"
    else:
        trend = "NO CHANGE"

    print("\nStatistics:")
    print("Average:", round(average, 2))
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Trend:", trend)

    # Simple letter grade
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

    if average >= 60:
        print("Status: PASSING")
    else:
        print("Status: FAILING")

    if improvement > 10:
        print("Performance: Improvement shown")
    elif improvement < -10:
        print("Performance: Decline shown")
    else:
        print("Performance: Stable overall")
else:
    print("\nRecord is invalid. Statistics not available.")
#problem 4
print("=== EVENT SCHEDULING SYSTEM ===")

# Event 1
print("\nEVENT 1 DETAILS:")
event1_name = input("Event name: ")
event1_day = input("Day (Mon-Sun): ").lower()[:3]
event1_start = float(input("Start time (0-24): "))
event1_end = float(input("End time (0-24): "))

# Event 2
print("\nEVENT 2 DETAILS:")
event2_name = input("Event name: ")
event2_day = input("Day (Mon-Sun): ").lower()[:3]
event2_start = float(input("Start time (0-24): "))
event2_end = float(input("End time (0-24): "))

# Valid days
valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# 1. Validate times are in range 0-24
event1_valid = (event1_start >= 0 and event1_end <= 24 and event1_end > event1_start and event1_day in valid_days)
event2_valid = (event2_start >= 0 and event2_end <= 24 and event2_end > event2_start and event2_day in valid_days)

print("\nSchedule Analysis:")

if event1_valid and event2_valid:
    print("Both events have valid times")
else:
    print("One or both events have invalid times")

# 2. Check for conflicts
same_day = (event1_day == event2_day)

overlap = (same_day and (event1_start < event2_end) and (event2_start < event1_end))

# Back-to-back events (less than 30 minutes = 0.5 hours)
gap = None
back_to_back = False

if same_day:
    if event1_end <= event2_start:
        gap = event2_start - event1_end
    elif event2_end <= event1_start:
        gap = event1_start - event2_end

    if gap is not None and gap < 0.5 and gap >= 0:
        back_to_back = True

# Early/late check
too_early_1 = event1_start < 6 or event1_end < 6
too_early_2 = event2_start < 6 or event2_end < 6
too_late_1 = event1_start > 23 or event1_end > 23
too_late_2 = event2_start > 23 or event2_end > 23

if overlap:
    print("Events overlap")
else:
    print("No direct overlap")

if same_day and back_to_back:
    print("Events are back-to-back")

if too_early_1 or too_early_2:
    print("One or more events are scheduled very early")

if too_late_1 or too_late_2:
    print("One or more events are scheduled very late")

# 4. Calculate total time commitment
if event1_valid and event2_valid:
    event1_length = event1_end - event1_start
    event2_length = event2_end - event2_start

    print("\nEvent 1:", event1_name)
    print(event1_day.title(), event1_start, "-", event1_end, "(", event1_length, "hours )")

    print("\nEvent 2:", event2_name)
    print(event2_day.title(), event2_start, "-", event2_end, "(", event2_length, "hours )")

    total_time = event1_length + event2_length
    print("\nTotal time commitment:", total_time, "hours")

    # 5. Scheduling recommendations
    if overlap:
        print("Recommendation: One event should be moved to avoid conflict")
    elif back_to_back:
        print("Recommendation: Add some break time between events")
    elif too_early_1 or too_early_2:
        print("Recommendation: Avoid scheduling events this early")
    elif too_late_1 or too_late_2:
        print("Recommendation: Try scheduling events earlier")
    else:
        print("Recommendation: Schedule looks fine")

else:
    print("\nCannot calculate time because event information was not valid")