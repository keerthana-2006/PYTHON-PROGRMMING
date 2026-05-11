'''
2. Basic Syntax and Variables
Explanation: Variables store data values. Python uses dynamic typing, meaning variables can change type. Variable names are case-sensitive and can contain letters, numbers, underscores.

Rules:
------
Must start with letter or underscore
Cannot start with number
Cannot use reserved keywords
'''
#Example code

# Variable assignment
x = 5               # Integer
name = "Alice"      # String
pi = 3.14159        # Float
is_valid = True     # Boolean

# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3

# Same value to multiple variables
x = y = z = 10

# Type checking
print(type(x))      # <class 'int'>
print(type(name))   # <class 'str'>

# Type conversion (casting)
num_str = "123"
num_int = int(num_str)   # String to integer
num_float = float(num_str)  # String to float
str_num = str(456)      # Integer to string

# Variable deletion
temp_var = 100
del temp_var
# print(temp_var)  # NameError: name 'temp_var' is not defined
