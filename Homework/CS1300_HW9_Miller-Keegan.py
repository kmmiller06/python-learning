#Problem 1
# ================================
# Problem 1: Temperature Converter
# ================================

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # Formula: F = C * 9/5 + 32
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    # Formula: C = (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def temperature_report(temp, scale="C"):
    """
    Print temperature in both scales.
    If scale is "C", convert to F.
    If scale is "F", convert to C.
    """
    if scale == "C":
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {converted}°F")
    else:
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {converted}°C")


# ---- Test Cases ----

# Test 1
print(celsius_to_fahrenheit(0))     # 32.0
print(celsius_to_fahrenheit(100))   # 212.0

# Test 2
print(fahrenheit_to_celsius(32))    # 0.0
print(fahrenheit_to_celsius(68))    # 20.0

# Test 3
temperature_report(25)         # 25°C = 77°F
temperature_report(77, "F")    # 77°F = 25°C

#Problem 2
# =====================================
# Problem 2: Weighted Grade Calculator
# =====================================

def calculate_weighted_grade(homework, midterm, final,
                             hw_weight=0.3, mid_weight=0.3, final_weight=0.4):
    """Calculate the weighted grade using the given weights."""
    weighted = (homework * hw_weight) + (midterm * mid_weight) + (final * final_weight)
    return weighted

def get_letter_grade(score):
    """Convert numeric score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def print_grade_report(name, hw, mid, final):
    """Print a full grade report for a student."""
    print("=== Grade Report ===")
    print("Student:", name)
    print("Homework:", hw)
    print("Midterm:", mid)
    print("Final:", final)

    weighted = calculate_weighted_grade(hw, mid, final)
    letter = get_letter_grade(weighted)

    print("Weighted Average:", round(weighted, 1))
    print("Letter Grade:", letter)
    print("--------------------")


# ---- Test Cases ----

grade1 = calculate_weighted_grade(85, 78, 92)
print("Grade 1:", grade1)   # ~85.9

grade2 = calculate_weighted_grade(90, 85, 80, hw_weight=0.4, mid_weight=0.2, final_weight=0.4)
print("Grade 2:", grade2)   # 86.0

print_grade_report("Alice Smith", 88, 91, 85)

#Problem 3
# =============================
# Problem 3: Fixing Scope Issues
# =============================

# These variables need to be global so all functions can modify them.
total_points = 0
bonus_multiplier = 1.1

def add_score(points):
    """Add points to total score."""
    global total_points      # Needed so we can update the global variable
    total_points = total_points + points
    return total_points

def apply_bonus():
    """Apply bonus multiplier to the score."""
    global total_points      # Needed so we modify the global total_points
    total_points = total_points * bonus_multiplier

def get_final_score():
    """Return the current total score."""
    # No 'global' needed here because we are only accessing it, not changing it.
    return total_points

def reset_game():
    """Reset the game score back to zero."""
    global total_points      # We are modifying the global variable
    total_points = 0


# ---- Test the fixed functions ----

reset_game()
add_score(100)
add_score(50)
apply_bonus()

print("Final score:", get_final_score())  # Should print 165.0