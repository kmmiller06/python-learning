# exercise4.py
# Order of Operations Practice
# Keegan Miller
# 8/25/25
# TODO: Predict the result BEFORE running each expression
# Write your prediction as a comment, then check if correct
# Expression 1
# Prediction: 2 + 12 = 14
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")
# Expression 2
# Prediction: 5 * 4 = 20
result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")
# Expression 3
# Prediction: 5 * 3 = 15.0
result3 = 10 / 2 * 3
print(f"10 / 2 * 3 = {result3}")
# Expression 4
# Prediction: 10/ 6 = 1.666...
result4 = 10 / (2 * 3)
print(f"10 / (2 * 3) = {result4}")
# Expression 5
# Prediction: 2 ** 9 = 512
result5 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result5}")
print("(Note: Exponentiation is right-to-left!)")
# Expression 6
# Prediction: 2 ** 9 = 512
result6 = 2 ** (3 ** 2)
print(f"2 ** (3 ** 2) = {result6}")
# TODO: Create your own complex expression
# Use at least 4 operations
my_expression = (2 + 1) * 2 ** 2 - 15 / 5
print(f"My expression: {my_expression}")
# TODO: Break down a complex expression step by step
complex = 10 + 20 * 30 / 10 - 5 ** 2
print("\nStep-by-step evaluation of: 10 + 20 * 30 / 10 - 5 ** 2")
print("Step 1: 5 ** 2 = 25")
print("Step 2: 20 * 30 = 600")
print("Step 3: 600 / 10 = 60.0")
print("Step 4: 10 + 60.0 = 70.0")
print("Step 5: 70.0 - 25 = 45.0")
print(f"Final result: {complex}")
