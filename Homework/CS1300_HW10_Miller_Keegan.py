# Problem 1: Statistics Calculator
def get_numbers():
    """
Get numbers from user until they enter 'done'.
Return list of floats.
    """
    numbers = []
    # Your code here
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    # Use input(), float() conversion
    # Handle 'done' to stop
    return numbers


def calculate_stats(numbers):
    """
Calculate min, max, average, and range.
Return all four values.
    """
    # Use built-in functions: min(), max(), sum(), len()
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    range_val = maximum - minimum
    # Return all four values
    return minimum, maximum, average, range_val


def format_stats(minimum, maximum, average, range_val):
    """
Format statistics for display.
Return formatted string.
    """
    # Use round() for 2 decimal places
    # Create formatted output string
    result = ""
    result += "Minimum: " + str(round(minimum, 2)) + "\n"
    result += "Maximum: " + str(round(maximum, 2)) + "\n"
    result += "Average: " + str(round(average, 2)) + "\n"
    result += "Range: " + str(round(range_val, 2))
    return result


def main():
    """Main program using modular design"""
    print("=== Statistics Calculator ===")
    # Call functions in order:
    # 1. Get numbers
    numbers = get_numbers()
    if not numbers:
        print("No numbers entered.")
        return
    # 2. Calculate stats
    minimum, maximum, average, range_val = calculate_stats(numbers)
    # 3. Format output
    output = format_stats(minimum, maximum, average, range_val)
    # 4. Display result
    print(output)

    minimum = min(numbers)

# Problem 2

def validate_score(score_str):
    """
Helper: Validate that string is valid score (0-100).
Return True/False.
"""
# Check if string is digit
    if not score_str.isdigit():
        return False
    # Check if in range 0-100
    score = int(score_str)
    return 0 <= score <= 100


def get_valid_score(prompt):
    """
Helper: Get validated score from user.
Keep asking until valid.
"""
    # Use validate_score() helper
    while True:
        score_str = input(prompt)
        if validate_score(score_str):
            return int(score_str)
        print("Invalid score. Please enter a number between 0 and 100.")
    # Keep looping until valid input
    # Return integer score


def calculate_letter(score):
    """
    Helper: Convert score to letter grade.
    """
    # A: >= 90, B: >= 80, C: >= 70, D: >= 60, F: < 60
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


def process_student():
    """
Process one student's grades.
Get 3 test scores, calculate average and letter.
    """
    # Use helper functions
    name = input("Enter student name: ")
    scores = []
    # Get name and 3 scores
    for i in range(1, 4):
        score = get_valid_score(f"Enter score for Test {i}: ")
        scores.append(score)
    # Calculate and return results
    average = sum(scores) / 3
    letter = calculate_letter(average)
    return name, scores, average, letter


def display_report(name, scores, average, letter):
    """
Display formatted student report.
    """
    print("----- Student Report -----")
    print("Name:", name)
    print("Scores:", scores)
    print("Average:", round(average, 2))
    print("Letter Grade:", letter)


def main():
    """
Main program - process multiple students.
    """
    # Ask how many students
    num_students = int(input("Enter number of students to process: "))
    for _ in range(num_students):
        name, scores, average, letter = process_student()
        display_report(name, scores, average, letter)
    # Process each student
    # Optional: Calculate class average

# Problem 3 - Fixing bad design

def shopping():
    items = []
    prices = []
    while True:
        item = input("Item (or done): ")
        if item == "done":
            break
        price = float(input("Price: "))
        items.append(item)
        prices.append(price)

    total = 0
    for p in prices:
        total = total + p

    print("Shopping List:")
    for i in range(len(items)):
        print(f"{items[i]}: ${prices[i]}")

    print(f"Total: ${total}")

    if total > 50:
        discount = total * 0.1
        total = total - discount
        print(f"10% discount: -${discount}")
        print(f"Final: ${total}")
