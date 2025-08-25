# exercise3.py
# Arithmetic Operations Lab
# Keegan Miller
# 8/25/25
# Test numbers
a = 17
b = 5
c = 2.5
print("Test Values:")
print(f"a = {a}, b = {b}, c = {c}")
print("-" * 30)
# TODO: Perform each operation and observe results
# Addition
add_result = a + b
print(f"{a} + {b} = {add_result}")
# Subtraction
subtract_result = a - b
print(f"{a} - {b} = {subtract_result}")
# Multiplication
multiply_result = a * b
print(f"{a} * {b} = {multiply_result}")
# Division (/) - note the type!
div_result = a / b
print(f"{a} / {b} = {div_result} (Type: {type(div_result)})")
# Integer Division (//)
print(f"{a} // {b} = {a // b}")
# Modulo (%)
print(f"{a} % {b} = {a % b}")
# Exponentiation (**)
print(f"{a} ** {b} = {a ** b}") 

print("-" * 30)
# TODO: Mixed type operations
print("Mixed Type Operations:")
# What happens with int + float?
mixed1 = a + c
print(f"{a} + {c} = {mixed1} (Type: {type(mixed1)})")
# Try more mixed operations
mixed2 = a * c
print(f"{a} * {c} = {mixed2} (Type: {type(mixed2)})")
# TODO: Special cases to explore
print("\nSpecial Cases:")
# Large numbers
big = 10 ** 100 # 10 to the power of 100
print(f"10^100 = {big}")
print(f"Python handles large numbers: {type(big)}")
# Negative division
neg_result = -17 // 5
print(f"-17 // 5 = {neg_result} (Note: rounds DOWN)")
# Division by zero (uncomment to see error)
# error_result = 10 / 0
