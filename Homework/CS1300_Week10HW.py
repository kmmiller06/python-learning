print('''
Week 10 Homework Problems
Keegan Miller 
CS1300
''')
print("Problem 1: Temperature Analyzer")
print("TEMPERATURE ANALYSIS REPORT \n==========================")
#1. Start with this list of temperatures (in Fahrenheit):
temps = [72, 68, 75, 71, 69, 77, 74, 70, 73, 76]
for i, temp in enumerate(temps):
    celsius = (temp - 32) * 5/9
    print(f"Day {i + 1}: {temp}°F ({celsius:.1f}°C)")

#2. Using for loops, calculate and print:  
#The average temperature
total_temp = 0
for temp in temps:
    total_temp += temp
average_temp = total_temp / len(temps)
print(f"Average Temperature: {average_temp:.1f}°F")
#The highest temperature
highest_temp = temps[0]
for temp in temps:
    if temp > highest_temp:
        highest_temp = temp
print(f"Highest Temperature: {highest_temp}°F")
#The lowest temperature
lowest_temp = temps[0]
for temp in temps:
    if temp < lowest_temp:
        lowest_temp = temp
print(f"Lowest Temperature: {lowest_temp}°F")
#How many days were above 72°F
days_above_72 = 0
for temp in temps:
    if temp > 72:
        days_above_72 += 1
print(f"Days Above 72°F: {days_above_72} days")

#Problem 2
print("Problem 2: Number Guessing Game")
import random
print("NUMBER GUESSING GAME \n====================")
print("I'm thinking of a number between 1 and 20.")
print("You have 5 guesses!")

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
guesses = []

for attempt in range(5):
    guess = int(input(f"Guess {attempt + 1}: "))
    guesses.append(guess)

    if guess == secret_number:
        print(f"Correct! You got it in {attempt + 1} guesses!")

        # Give message based on number of attempts
        if attempt + 1 == 1:
            print("Amazing! You're a mind reader!")
        elif attempt + 1 <= 3:
            print("Great job!")
        else:
            print("Good work!")
        break
    elif guess < secret_number:
        print("Too low, try higher.")
    else:
        print("Too high, try lower.")
else:
    print("You've run out of guesses.")
    print(f"The number was {secret_number}.")
    print("Better luck next time!")

print(f"Your guesses were: {guesses}")

# Problem 3: Grade Processor

grades = [85, -10, 92, 150, 78, 0, 95, 88, -5, 100, 73, 200]

print("Processing Grades...")
print("==================")

valid = []
invalid_count = 0
distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

# Process grades
for grade in grades:
    # Skip invalid grades
    if grade < 0 or grade > 100:
        print(f"Skipping invalid grade: {grade}")
        invalid_count += 1
        continue
    
    valid.append(grade)
    grade_num = len(valid)

    # Determine letter grade
    if grade >= 90:
        letter = "A"
        distribution["A"] += 1
    elif grade >= 80:
        letter = "B"
        distribution["B"] += 1
    elif grade >= 70:
        letter = "C"
        distribution["C"] += 1
    elif grade >= 60:
        letter = "D"
        distribution["D"] += 1
    else:
        letter = "F"
        distribution["F"] += 1

    print(f"Grade {grade_num}: {grade} ({letter})")
    
    

# Summary Report
print("\nSummary Report")
print("==============")
print(f"Total grades processed: {len(valid)}")
print(f"Invalid grades skipped: {invalid_count}")

print("Grade Distribution:")
for letter, count in distribution.items():
    print(f"{letter}: {count} students")

if valid:
    average = sum(valid) / len(valid)
    print(f"Class Average: {average:.1f}")
else:
    print("No valid grades to calculate average.")
