
# exercise2.py
# Type Detective
# Keegan Miller
# 8/25/25
# Mystery variables - determine their types!
mystery1 = 42
mystery2 = "42"
mystery3 = 42.0
mystery4 = "42.0"
mystery5 = True
mystery6 = "True"
# TODO: Print each mystery variable and its type
print("Mystery 1:", mystery1, "is type:", type(mystery1))
print("Mystery 2:", mystery2, "is type:", type(mystery2))
print("Mystery 3:", mystery3, "is type:", type(mystery3))
print("Mystery 4:", mystery4, "is type:", type(mystery4))
print("Mystery 5:", mystery5, "is type:", type(mystery5))
print("Mystery 6:", mystery6, "is type:", type(mystery6))

# Continue for all mystery variables...
# TODO: Predictions - Before running, write what you think will happen
# Then run and check if you were correct
# Prediction 1: What is mystery1 + mystery3?
# Your prediction: 42+ 42.0 = 84.0
result1 = mystery1 + mystery3
print("mystery1 + mystery3 =", result1, "Type:", type(result1))
# Prediction 2: What is mystery2 + mystery4?
# Your prediction: "42" + "42.0" = "4242.0"
result2 = mystery2 + mystery4
print("mystery2 + mystery4 =", result2, "Type:", type(result2))
# TODO: Convert mystery2 to an integer and add to mystery1
converted = int(mystery2)
sum_result = mystery1 + converted
print("Converted sum:", sum_result)
# TODO: Convert mystery5 to an integer - what value do you get?
bool_as_int = int(mystery5)
print("True as integer:", bool_as_int)
# CHALLENGE: Can you convert mystery6 to a boolean? What do you get?
bool_from_str = bool(mystery6)
print("mystery6 ('True') as boolean:", bool_from_str)