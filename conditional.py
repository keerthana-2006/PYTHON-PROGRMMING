'''
5. Control Flow
Explanation: Control flow statements determine the order in which code executes based on conditions or loops.
'''
#Conditional Statements
#---------------------
#python
# if statement
age = 18
if age >= 18:
    print("Adult")

# if-else
score = 75
if score >= 60:
    print("Passed")
else:
    print("Failed")

# if-elif-else
grade = 85
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
print(f"Grade: {letter}")

# Nested if
x = 10
if x > 0:
    if x < 20:
        print("Positive and less than 20")

# Ternary operator (conditional expression)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Multiple conditions
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
