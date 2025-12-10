#Problem 1
from ast import pattern


def count_positive(numbers):
    """
    Count how many positive numbers (greater than 0) are in the list.
    
    Parameters:
        numbers: a list of numbers
    
    Returns:
        The count of positive numbers
    """
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count
#Test function
print(count_positive([5, -2, 0, 3, -1, 8]))  # 3
print(count_positive([-1,-2, -3]))          # 0
print(count_positive([10, 20, 30]))          # 3
print(count_positive([]))                    # 0

#problem 2
def get_age_group(age):
    """
    Classify age into a group.
    0-12: Child
    13-19: Teen
    20-59: Adult
    60+: Senior

    Parameters
    age: Person's age (integer)
    Returns:
    Age group as a string
   """
    # Your code here
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    elif age >= 60:
        return "Senior"
def count_age_groups(ages):
    """
    Count how many people in each age group.
    Parameters:
    ages: List of ages
    Returns:
    Dictionary with counts for each group
    """
    groups = {"Child": 0, "Teen": 0, "Adult": 0, "Senior": 0}
    for age in ages:
        group = get_age_group(age)
        groups[group] += 1
    # For each age, get its group and increment count
    return groups
print(get_age_group(5)) # Should print: Child
print(get_age_group(15)) # Should print: Teen
print(get_age_group(30)) # Should print: Adult
print(get_age_group(65)) # Should print: Senior
ages_list = [5, 15, 25, 35, 65, 8, 18, 70]
print(count_age_groups(ages_list)) # Should show counts for each group

#Problem 3
def is_palindrome(word):
    """
    Check if a word is a palindrome (same forwards and backwards).
    Case-insensitive.
    Parameters:
    word: String to check
    Returns:
    True if palindrome, False otherwise
    """
    # Convert to lowercase
    word = word.lower()
    # Your code here
    reversed_word = word[::-1]
    return word == reversed_word
# Test your function:
print(is_palindrome("racecar")) # Should print: True
print(is_palindrome("hello")) # Should print: False
print(is_palindrome("Mom")) # Should print: True
print(is_palindrome("noon")) # Should print: True
print(is_palindrome("python")) # Should print: False
