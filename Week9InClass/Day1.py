numbers = [12, 5, 18, 3, 20, 7]
# Write a loop that prints each number and whether it's:    
# - Greater than 10: "big"
# - 5 to 10: "medium"
# - Less than 5: "small"

for num in numbers:
    if num > 10:
        print(f"{num} is big")
    elif 5 <= num <= 10:
        print(f"{num} is medium")
    else:
        print(f"{num} is small")