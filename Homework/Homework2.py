# CS 1300 - Homework 2
# Name: Keegan Miller
# Date: 9/18/25
# Description: Variables, Input/Output, and Type Conversions

#Problem 1
print("\n" + "=" * 40)
print("Problem 1: Personal Finance Calculator")
print("=" * 40)

income = float(input("Enter monthly income: "))
rent = float(input("Enter rent cost: "))
food = float(input("Enter food expenses: "))
transportation = float(input("Enter transportation cost: "))
other = float(input("Enter other expenses: "))
total = income + rent + food + transportation + other
balance = income - rent - food - transportation - other
savings_rate = balance / income 

print(f"{"=" * 40}")
print("Monthly Budget Report")
print(f"{"=" * 40}")
print(f"Income: ${income}")
print(f"{"-" * 40}")
print(f"Expenses: \n Housing: ${rent} \n Food: ${food} \n Transportation ${transportation} \n Other: ${other}")
print(f"{"-" * 40}")
print(f"Total expenses: ${total} \n Remaining Balance: ${balance} \n Savings Rate: {savings_rate}% ")
print(f"{"=" * 40}")
