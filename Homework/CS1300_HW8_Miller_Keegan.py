#Problem 1
print("Problem 1: Multiplication Table Generator \n ===================")
table_size = int(input("What is the table size (1-12)"))
#validate using a while loop
while table_size < 0 or table_size > 12:
    print("Invalid table size, please enter a size between 1-12")
    table_size = int(input("What is the table size (1-12): "))
#use nested for loops to generate the table
print(f"Multiplication Table ({table_size}x{table_size}):")
for i in range(1, table_size + 1):
    for j in range(1, table_size + 1):
        product = i * j
        print(f"{product:4}", end="")
    print()  # New line after each row
    
    #Problem 2   
print("=== PATTERN ANALYSIS ===")

# Original numbers list
numbers = [23, 8, 45, 12, 78, 34, 67, 91, 15, 52, 41, 3]
print(f"Original numbers: {numbers}")

print("1. Search Pattern \n First Number > 75:")

first_over_75 = None
position = None



for i, num in enumerate(numbers):
    if num > 75:
        first_over_75 = num
        position = i
        break

print(f"First number > 75: {first_over_75} (at position {position})")

# Filter Pattern
print("2. Filter Pattern \n Even Numbers:")

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)

# Counter Pattern
print("3. Counter Pattern \n Number Ranges:")

range_0_25 = 0
range_26_50 = 0
range_51_75 = 0
range_76_100 = 0

for num in numbers:
    if 0 <= num <= 25:
        range_0_25 += 1
    elif 26 <= num <= 50:
        range_26_50 += 1
    elif 51 <= num <= 75:
        range_51_75 += 1
    elif 76 <= num <= 100:
        range_76_100 += 1

print(f"Range 0-25: {range_0_25} numbers")
print(f"Range 26-50: {range_26_50} numbers")
print(f"Range 51-75: {range_51_75} numbers")
print(f"Range 76-100: {range_76_100} numbers")

# Accumulator Pattern
print("4. Accumulator Pattern \n Sum of Numbers Divisible by 3:")

divisible_by_3 = []
sum_divisible = 0

for num in numbers:
    if num % 3 == 0:
        divisible_by_3.append(num)
        sum_divisible += num

print("Numbers divisible by 3:", divisible_by_3)
print("Sum of these numbers:", sum_divisible)

# Sentinel Pattern
print("5. Sentinel Pattern \n Add More Numbers:")
print("Add more numbers (enter -1 to stop):")

while True:
    user_input = int(input("Enter number: "))
    if user_input == -1:
        break
    numbers.append(user_input)

print("Updated list:", numbers)
print("New count:", len(numbers), "numbers")

#Problem 3
# ============================================
# GRADE REPORT SYSTEM
# ============================================

students = ["Alice", "Bob", "Carol", "David", "Emma"]

grades = {
    "Alice":  [92, 88, 95, 87, 90],
    "Bob":    [78, 82, 73, 85, 80],
    "Carol":  [95, 91, 98, 92, 94],
    "David":  [65, 70, 68, 72, 75],
    "Emma":   [88, 85, 82, 90, 87]
}

assignments = ["HW1", "HW2", "Quiz1", "Exam1", "Quiz2"]

print("=== GRADE REPORT SYSTEM ===\n")

# ----------------------------------------------------
# 1. GRADE TABLE (with nested loops)
# ----------------------------------------------------
print("Grade Table:")
print("HW1 HW2 Quiz1 Exam1 Quiz2  AVG  Grade")
print("-" * 60)

student_averages = {}
letter_grades = {}

for student in students:
    scores = grades[student]
    avg = sum(scores) / len(scores)
    student_averages[student] = avg

    # Determine letter grade
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    letter_grades[student] = grade

    # Print row using nested loop
    for score in scores:
        print(f"{score:<5}", end="")
    print(f"{avg:>6.1f}  {grade}")

print()

# ----------------------------------------------------
# 2. ASSIGNMENT STATISTICS
# ----------------------------------------------------
print("Assignment Statistics:")

for i, assign in enumerate(assignments):
    all_scores = [grades[s][i] for s in students]
    avg = sum(all_scores) / len(all_scores)
    high = max(all_scores)
    low = min(all_scores)

    # Find student names for high/low
    high_student = [s for s in students if grades[s][i] == high][0]
    low_student = [s for s in students if grades[s][i] == low][0]

    print(f"{assign}: Class Avg: {avg:.1f} Highest: {high} ({high_student}) Lowest: {low} ({low_student})")

print()

# ----------------------------------------------------
# 3. HONOR ROLL & ACADEMIC WARNING
# ----------------------------------------------------
honor_roll = [s for s in students if student_averages[s] >= 90]
warnings = [s for s in students if student_averages[s] < 70]

print("Special Recognition:")
print("Honor Roll (90+ average):", ", ".join(honor_roll) if honor_roll else "None")
print("Academic Warning (<70 average):", ", ".join(warnings) if warnings else "None")
print()

# ----------------------------------------------------
# 4. CLASS SUMMARY
# ----------------------------------------------------
highest_student = max(student_averages, key=student_averages.get)
lowest_student = min(student_averages, key=student_averages.get)
class_average = sum(student_averages.values()) / len(student_averages)

print("Class Summary:")
print(f"Highest Overall Average: {highest_student} ({student_averages[highest_student]:.1f}%)")
print(f"Lowest Overall Average: {lowest_student} ({student_averages[lowest_student]:.1f}%)")
print(f"Class Average: {class_average:.1f}%")
print()

# ----------------------------------------------------
# 5. GRADE DISTRIBUTION
# ----------------------------------------------------
distribution = {"A":0, "B":0, "C":0, "D":0, "F":0}
for grade in letter_grades.values():
    distribution[grade] += 1

print("Grade Distribution:")
for grade, count in distribution.items():
    print(f"{grade}: {count} student(s)")
