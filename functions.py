'''
6. Functions
Explanation: Functions are reusable blocks of code that perform specific tasks. They help organize code, avoid repetition, and improve maintainability.
'''

#Function Definition and Calling

# Basic function
def greet():
    print("Hello!")

greet()  # Call function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Function with default arguments
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (uses default exponent)
print(power(2, 3))   # 8

# Keyword arguments
def introduce(name, age, city):
    print(f"{name} is {age} years old from {city}")

introduce(age=25, city="New York", name="Bob")

# Variable number of arguments (*args)
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# Variable number of keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, job="Engineer")

# Combining arguments
def complex_func(a, b, *args, option="default", **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"option={option}")
    print(f"kwargs={kwargs}")

complex_func(1, 2, 3, 4, 5, option="custom", x=10, y=20)
