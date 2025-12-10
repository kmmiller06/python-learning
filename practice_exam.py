def count_even(numbers):
    """
    Count how many even numbers are in the list.
    
    Parameters:
        numbers: a list of numbers
    
    Returns:
        The count of even numbers
    """
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count_even
    print()