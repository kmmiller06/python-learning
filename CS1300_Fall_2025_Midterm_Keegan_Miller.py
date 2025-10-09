#Problem 1
"""
Problem 1: String Processing
Complete each task below
"""

#given information (DO NOT MODIFY):
full_name = "John Michael Smith"
email = "john.smith@university.edu"
phone = "555-123-4567"

#Task 1.1: Extract and print the first name only
first_name = full_name.split()[0]
print(f"First name: {first_name}")
#Task 1.2: Extract and print the last name only
last_name = full_name.split()[-1]
print(f"Last name: {last_name}")
#Task 1.3: Create and print initials (J.M.S)
initials = f"{full_name[0]}.{full_name[5]}.{full_name[13]}"
print(f"Initials: {initials}")
#Task 1.4: Check if the email contains "university" (case insensitive)
contains_university = "university" in email.lower()
print(f"Email contains 'university': {contains_university}")
#Task 1.5: Replace all dashes in the phone number with spaces and print
formatted_phone = phone.replace('-', ' ')
print(f"Formatted phone: {formatted_phone}")

#Problem 3
"""
Problem 3: Movie Review Number management
Manage a list of movie review numbers.
"""

# Task 3.1 (2 points): Create a list with these movie review numbers
numbers = [3, 5, 4, 3, 2, 1, 3]
print(f"Movie reviews: {numbers}")
# Task 3.2 (3 points): Add a new review number of 4 to the end
numbers.extend([4])
print(f"Updated movie reviews: {numbers}")
# Task 3.3 (3 points): The third review number (4) was entered wrong.
# Change it to 3    
numbers[2] = 3
print(f"Updated movie reviews: {numbers}")
# Task 3.4 (3 points): Remove the review number 1 from the list
numbers.remove(3)
print(f"Updated movie reviews: {numbers}")
# Task 3.5 (3 points): Insert a review number of 3 at position 2
numbers.insert(2, 3)
print(f"Updated movie reviews: {numbers}")
# Task 3.6 (3 points): Create and print a sublist of the first 3 numbers
sublist = numbers[:3]
print(f"Sublist of first 3 numbers: {sublist}")
# Task 3.7 (3 points): Print:
# - How many movie review numbers
# - The first review number
# - The last review number
print(f"Total movie reviews: {len(numbers)}")
print(f"First movie review: {numbers[0]}")
print(f"Last movie review: {numbers[-1]}")
