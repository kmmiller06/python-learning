def greet(name):
    print(f"Hello, {name}!")
# Call it here with your name
greet("Keegan Miller")

# Define function here
def double(n):
    print(f"{n * 2}")
# Call it with 5
double(5)

# Should print: "Hi, I'm John Doe and I'm 18 years old."
def introduce(first_name, last_name, age):
    print(f"Hi, I'm {first_name} {last_name} and I'm {age} years old.")
introduce(first_name= "John", last_name= "Doe", age= 18)


def greet(first, last="User", title=""):
    print(f"{title} {first} {last}")
# Mark each as VALID or INVALID:
# A. greet("John") Valid
# B. greet(first="John") Valid
# C. greet("John", "Doe", "Mr.") Valid
# D. greet(title="Ms.", "Jane") Invalid

