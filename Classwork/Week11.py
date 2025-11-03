# This should print only positive odd numbers
numbers = [1, -3, 4, 5, -7, 8, 9]
for num in numbers:
# Add appropriate control statements
    if num > 0 and num % 2 != 0:
        print(num)  
        
# Rewrite this code using break and continue
# Task: Find first positive number divisible by 3
numbers = [1, -6, 7, 9, -12, 4]
result = None
for num in numbers:
    if result is None:
        if num > 0:
            if num % 3 == 0:
                result = num
                break
print(result)