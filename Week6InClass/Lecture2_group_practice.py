'''
Practice 1-a
'''
# TODO: Create a store system with these features:
# 1. Display a menu of 5 items with prices
# 2. Let user select one item
# 3. Ask for quantity
# 4. Apply discounts:
#    - 10+ items: 10% off
#    - Member: additional 5% off
# 5. Calculate tax (8%)
# 6. Show final receipt
#Your code here:

items = {
    "Apple": 0.5,
    "Banana": 0.3,
    "Orange": 0.4,
    "Mango": 0.6,
    "Grapes": 0.8
}

def calculate_total(item, quantity, is_member=False):
    if item not in items:
        return "Item not found."
   
    price = items[item] * quantity
    if quantity >= 10:
        price *= 0.9  # 10% discount
    if is_member:
        price *= 0.95  # additional 5% discount
   
    tax = price * 0.08  # 8% tax
    total = price + tax
    return total


print("=== CORNER STORE ===")
while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item == "done":
        break
    quantity = int(input("Enter quantity: "))
    is_member = input("Are you a member? (yes/no): ") == "yes"
    total = calculate_total(item, quantity, is_member)
    print(f"Total for {quantity} {item}(s): ${total:.2f}")

'''
Practice 1-b
'''

# TODO: Create a health advisor with these features:
# 1. Ask for age, weight, height
# 2. Ask about exercise (none/light/moderate/heavy)
# 3. Ask about sleep hours
# 4. Ask about water intake (glasses per day)
# 5. Calculate BMI
# 6. Provide personalized recommendations based on all inputs
# 7. Give an overall health score (0-100)

print("=== HEALTH ADVISOR ===")
# Your code here
def calculate_bmi(weight, height):
    return weight / (height ** 2) * 703  # BMI formula for pounds and inches
def health_score(age, exercise, sleep, water):
    score = 100
    if age < 18 or age > 65:
        score -= 10
    if exercise == "none":
        score -= 20
    elif exercise == "light":
        score -= 10
    elif exercise == "moderate":
        score -= 5
    if sleep < 6:
        score -= 15
    elif sleep > 9:
        score -= 5
    if water < 4:
        score -= 10
    elif water > 8:
        score += 5
    return max(0, min(100, score))
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (lbs): "))
height = float(input("Enter your height (inches): "))
exercise = input("Enter your exercise level (none/light/moderate/heavy): ")
sleep = float(input("Enter your average sleep hours per night: "))
water = float(input("Enter your average water intake (glasses per day): "))

bmi = calculate_bmi(weight, height)
health = health_score(age, exercise, sleep, water)

print(f"Your BMI is: {bmi:.2f}")
print(f"Your health score is: {health}")

'''
Practice 1-c
'''

# TODO: Create a character creator with:
# 1. Choose class (Warrior/Mage/Rogue)
# 2. Allocate 20 skill points among:
#    - Strength, Intelligence, Agility
# 3. Validate point allocation
# 4. Calculate derived stats:
#    - Health = 100 + (Strength * 10)
#    - Mana = 50 + (Intelligence * 15)
#    - Speed = 5 + (Agility * 2)
# 5. Assign starting equipment based on class
# 6. Display complete character sheet

print("=== CHARACTER CREATOR ===")
# Your code here
classes = {
    "Warrior": {"Strength": 10, "Intelligence": 5, "Agility": 5, "Equipment": "Sword and Shield"},
    "Mage": {"Strength": 5, "Intelligence": 10, "Agility": 5, "Equipment": "Staff and Spellbook"},
    "Rogue": {"Strength": 5, "Intelligence": 5, "Agility": 10, "Equipment": "Daggers and Lockpicks"}
}
def calculate_stats(strength, intelligence, agility):
    health = 100 + (strength * 10)
    mana = 50 + (intelligence * 15)
    speed = 5 + (agility * 2)
    return health, mana, speed
print("Choose your class (Warrior/Mage/Rogue): ")
chosen_class = input()
if chosen_class not in classes:
    print("Invalid class.")
else:
    print("You have 20 skill points to allocate among Strength, Intelligence, and Agility.")
    points = 20
    strength = int(input("Allocate points to Strength: "))
    intelligence = int(input("Allocate points to Intelligence: "))
    agility = int(input("Allocate points to Agility: "))
    if strength + intelligence + agility != points:
        print("Invalid point allocation.")
    else:
        health, mana, speed = calculate_stats(strength, intelligence, agility)
        equipment = classes[chosen_class]["Equipment"]
        print("\n=== CHARACTER SHEET ===")
        print(f"Class: {chosen_class}")
        print(f"Strength: {strength}")
        print(f"Intelligence: {intelligence}")
        print(f"Agility: {agility}")
        print(f"Health: {health}")
        print(f"Mana: {mana}")
        print(f"Speed: {speed}")
        print(f"Starting Equipment: {equipment}")


'''
Practice 2-a
'''
# TODO: Create a contact form with validation for:
# 1. Name (required, 2-50 chars)
# 2. Email (must contain @ and .)
# 3. Subject (required, max 100 chars)
# 4. Message (required, 10-500 chars)
# 5. Show all errors at once with helpful messages

print("=== CONTACT FORM ===")
# Your code here:
def validate_contact_form(name, email, subject, message):
    errors = []
    if not (2 <= len(name) <= 50):
        errors.append("Name must be between 2 and 50 characters.")
    if "@" not in email or "." not in email:
        errors.append("Email must contain '@' and '.'.")
    if not subject or len(subject) > 100:
        errors.append("Subject is required and must be less than 100 characters.")
    if not (10 <= len(message) <= 500):
        errors.append("Message must be between 10 and 500 characters.")
    return errors
name = input("Enter your name: ")
email = input("Enter your email: ")
subject = input("Enter the subject: ")
message = input("Enter your message: ")
errors = validate_contact_form(name, email, subject, message)
if errors:
    print("Please correct the following errors:")
    for error in errors:
        print(f"- {error}")
else:
    print("Form submitted successfully!")



'''
Practice 2-b
'''
# TODO: Create credit card validator with:
# 1. Card number (16 digits)
# 2. Detect card type (Visa starts with 4, Mastercard with 5)
# 3. Expiry date (MM/YY format, not expired)
# 4. CVV (3 or 4 digits)
# 5. Cardholder name (letters and spaces only)
# 6. Billing ZIP (5 digits)
# Show validation status for each field

print("=== PAYMENT VALIDATION ===")
# Your code here:
import re
from datetime import datetime
def validate_credit_card(number, expiry, cvv, name, zip_code):
    errors = []
    if not re.fullmatch(r"\d{16}", number):
        errors.append("Card number must be 16 digits.")
    elif number.startswith("4"):
        card_type = "Visa"
    elif number.startswith("5"):
        card_type = "Mastercard"
    else:
        errors.append("Card type not recognized.")
   
    try:
        exp_date = datetime.strptime(expiry, "%m/%y")
        if exp_date < datetime.now():
            errors.append("Card is expired.")
    except ValueError:
        errors.append("Expiry date must be in MM/YY format.")
   
    if not re.fullmatch(r"\d{3,4}", cvv):
        errors.append("CVV must be 3 or 4 digits.")
   
    if not re.fullmatch(r"[A-Za-z ]+", name):
        errors.append("Cardholder name must contain only letters and spaces.")
   
    if not re.fullmatch(r"\d{5}", zip_code):
        errors.append("Billing ZIP must be 5 digits.")
   
    return errors, card_type if 'card_type' in locals() else None
card_number = input("Enter card number (16 digits): ")
expiry_date = input("Enter expiry date (MM/YY): ")
cvv = input("Enter CVV (3 or 4 digits): ")
cardholder_name = input("Enter cardholder name: ")
billing_zip = input("Enter billing ZIP (5 digits): ")
errors, card_type = validate_credit_card(card_number, expiry_date, cvv, cardholder_name, billing_zip)
if errors:
    print("Please correct the following errors:")
    for error in errors:
        print(f"- {error}")
else:
    print(f"Card is valid. Type: {card_type}")
    print("Proceeding to payment...")





'''
Practice 2-c
'''
# TODO: Create student registration with:
# 1. Student ID (exactly 8 digits, starts with 2)
# 2. Full name (first, middle optional, last)
# 3. Email (must end with .edu)
# 4. Phone (optional but validate if provided)
# 5. Emergency contact (name and phone)
# 6. Course selection (pick 3-6 from list)
# 7. Validate no scheduling conflicts
# 8. Calculate tuition based on courses
# 9. Show complete registration summary

print("=== STUDENT REGISTRATION ===")
# Your code here
import re
def validate_student_registration(student_id, full_name, email, phone, emergency_contact, courses):
    errors = []
    if not re.fullmatch(r"2\d{7}", student_id):
        errors.append("Student ID must be exactly 8 digits and start with 2.")
   
    if not re.fullmatch(r"[A-Za-z]+( [A-Za-z]+)*", full_name):
        errors.append("Full name must contain only letters and spaces.")
   
    if not email.endswith(".edu") or "@" not in email:
        errors.append("Email must end with .edu and contain '@'.")
   
    if phone and not re.fullmatch(r"\d{10}", phone):
        errors.append("Phone number must be 10 digits if provided.")
   
    if not re.fullmatch(r"[A-Za-z ]+ \d{10}", emergency_contact):
        errors.append("Emergency contact must include name and a 10-digit phone number.")
   
    if not (3 <= len(courses) <= 6):
        errors.append("You must select between 3 and 6 courses.")
   
    # Placeholder for scheduling conflict check
    # In a real system, we would check course times here
   
    return errors
available_courses = ["Math 101", "History 201", "Biology 150", "Chemistry 110", "Physics 120", "English 101"]
student_id = input("Enter Student ID (8 digits, starts with 2): ")
full_name = input("Enter Full Name: ")
email = input("Enter Email (must end with .edu): ")
phone = input("Enter Phone (optional, 10 digits): ")
emergency_contact = input("Enter Emergency Contact (Name and 10-digit phone): ")
print("Available courses:")
for i, course in enumerate(available_courses, 1):
    print(f"{i}. {course}")
course_selection = input("Select courses (comma-separated numbers): ")



'''
Practice 3-a
'''
# TODO: Create a savings calculator that:
# 1. Asks for current savings
# 2. Asks for savings goal
# 3. Asks for monthly contribution
# 4. Calculates months to reach goal
# 5. Provides encouragement based on progress
# 6. Suggests ways to reach goal faster

print("=== SAVINGS GOAL TRACKER ===")
# Your code here:
def calculate_months_to_goal(current, goal, monthly):
    if monthly <= 0:
        return float('inf')  # Cannot reach goal with non-positive contributions
    months = 0
    while current < goal:
        current += monthly
        months += 1
    return months

current_savings = float(input("Enter your current savings: "))
savings_goal = float(input("Enter your savings goal: "))
monthly_contribution = float(input("Enter your monthly contribution: "))
months_needed = calculate_months_to_goal(current_savings, savings_goal, monthly_contribution)
if months_needed == float('inf'):
    print("Your monthly contribution must be positive.")
else:
    print(f"You need {months_needed} months to reach your savings goal.")
    if current_savings >= savings_goal:
        print("Congratulations! You've already reached your savings goal!")
    else:
        progress = (current_savings / savings_goal) * 100
        print(f"You're {progress:.2f}% towards your goal. Keep it up!")
        if months_needed > 12:
            print("Consider increasing your monthly contribution to reach your goal faster.")
        else:
            print("You're on track to reach your goal soon!")

'''
Practice 3-b
'''
# TODO: Create loan eligibility checker:
# 1. Get income, expenses, credit score
# 2. Calculate debt-to-income ratio
# 3. Check eligibility for different loan types:
#    - Personal (credit > 650, DTI < 40%)
#    - Auto (credit > 600, DTI < 45%)
#    - Mortgage (credit > 700, DTI < 35%)
# 4. Calculate maximum loan amount
# 5. Show interest rates based on credit score

print("=== LOAN ELIGIBILITY CHECKER ===")
# Your code here:
def calculate_dti(income, expenses):
    if income == 0:
        return float('inf')  # Avoid division by zero
    return (expenses / income) * 100
def check_loan_eligibility(credit_score, dti):
    eligibility = {}
    if credit_score > 650 and dti < 40:
        eligibility["Personal Loan"] = True
    else:
        eligibility["Personal Loan"] = False
    if credit_score > 600 and dti < 45:
        eligibility["Auto Loan"] = True
    else:
        eligibility["Auto Loan"] = False
    if credit_score > 700 and dti < 35:
        eligibility["Mortgage"] = True
    else:
        eligibility["Mortgage"] = False
    return eligibility
def max_loan_amount(income, dti):
    if dti == 0:
        return 0
    return (income * (dti / 100)) * 5  # Simplified formula
def interest_rate(credit_score):
    if credit_score >= 750:
        return 3.5
    elif credit_score >= 700:
        return 4.5
    elif credit_score >= 650:
        return 6.0
    elif credit_score >= 600:
        return 8.0
    else:
        return 12.0
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
credit_score = int(input("Enter your credit score: "))
dti = calculate_dti(income, expenses)
eligibility = check_loan_eligibility(credit_score, dti)
max_loan = max_loan_amount(income, dti)
rate = interest_rate(credit_score)
print(f"Your Debt-to-Income Ratio is: {dti:.2f}%")
print("Loan Eligibility:")
for loan_type, is_eligible in eligibility.items():
    status = "Eligible" if is_eligible else "Not Eligible"
    print(f"- {loan_type}: {status}")
print(f"Maximum Loan Amount you can apply for: ${max_loan:.2f}")
print(f"Estimated Interest Rate based on your credit score: {rate:.2f}%")




'''
Practice 3-c
'''
# TODO: Create investment portfolio system:
# 1. Input current age and retirement age
# 2. Enter current investments in:
#    - Stocks, Bonds, Real Estate, Cash
# 3. Calculate risk profile based on age
# 4. Analyze portfolio balance
# 5. Suggest rebalancing if needed
# 6. Project retirement readiness
# 7. Provide personalized recommendations

print("=== INVESTMENT PORTFOLIO ANALYZER ===")
# Your code here:
def risk_profile(age):
    if age < 30:
        return "High Risk"
    elif age < 50:
        return "Moderate Risk"
    else:
        return "Low Risk"
def analyze_portfolio(stocks, bonds, real_estate, cash):
    total = stocks + bonds + real_estate + cash
    if total == 0:
        return "No investments found."
    stock_pct = (stocks / total) * 100
    bond_pct = (bonds / total) * 100
    real_estate_pct = (real_estate / total) * 100
    cash_pct = (cash / total) * 100
    return stock_pct, bond_pct, real_estate_pct, cash_pct
def suggest_rebalancing(age, stock_pct):
    profile = risk_profile(age)
    if profile == "High Risk" and stock_pct < 70:
        return "Consider increasing your stock investments."
    elif profile == "Moderate Risk" and (stock_pct < 50 or stock_pct > 70):
        return "Consider rebalancing your portfolio to have 50-70% in stocks."
    elif profile == "Low Risk" and stock_pct > 50:
        return "Consider decreasing your stock investments."
    return "Your portfolio is well balanced."
def retirement_readiness(current_age, retirement_age, total_investments):
    years_to_retirement = retirement_age - current_age
    if years_to_retirement <= 0:
        return "You are at or past retirement age."
    required_savings = years_to_retirement * 10000  # Simplified assumption
    if total_investments >= required_savings:
        return "You are on track for retirement."
    else:
        return f"You need to save an additional ${required_savings - total_investments:.2f} for retirement."
current_age = int(input("Enter your current age: "))
retirement_age = int(input("Enter your desired retirement age: "))
stocks = float(input("Enter your investment in Stocks: "))
bonds = float(input("Enter your investment in Bonds: "))
real_estate = float(input("Enter your investment in Real Estate: "))
cash = float(input("Enter your investment in Cash: "))
portfolio_analysis = analyze_portfolio(stocks, bonds, real_estate, cash)
if isinstance(portfolio_analysis, str):
    print(portfolio_analysis)
else:
    stock_pct, bond_pct, real_estate_pct, cash_pct = portfolio_analysis
    print(f"Portfolio Distribution:\n- Stocks: {stock_pct:.2f}%\n- Bonds: {bond_pct:.2f}%\n- Real Estate: {real_estate_pct:.2f}%\n- Cash: {cash_pct:.2f}%")
    rebalancing_suggestion = suggest_rebalancing(current_age, stock_pct)
    print(rebalancing_suggestion)
    total_investments = stocks + bonds + real_estate + cash
    readiness = retirement_readiness(current_age, retirement_age, total_investments)
    print(readiness)
course_selection = input("Select courses by entering their numbers separated by commas: ")
course_selection_indices = [int(i)-1 for i in course_selection.split(",") if i.strip().isdigit() and 0 < int(i) <= len(available_courses)]
selected_courses = [available_courses[i] for i in course_selection_indices]

errors = validate_student_registration(student_id, full_name, email, phone, emergency_contact, selected_courses)
if errors:
    print("Please correct the following errors:")
    for error in errors:
        print(f"- {error}")
else:
    tuition_per_course = 300  # Example tuition per course
    total_tuition = len(selected_courses) * tuition_per_course
    print("\n=== REGISTRATION SUMMARY ===")
    print(f"Student ID: {student_id}")
    print(f"Full Name: {full_name}")
    print(f"Email: {email}")
    if phone:
        print(f"Phone: {phone}")
    print(f"Emergency Contact: {emergency_contact}")
    print("Selected Courses:")
    for course in selected_courses:
        print(f"- {course}")
    print(f"Total Tuition: ${total_tuition:.2f}")
    print("Registration completed successfully!")

print("="*40)