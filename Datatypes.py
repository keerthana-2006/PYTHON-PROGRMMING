'''
3. Data Types
Explanation: Python has several built-in data types for representing different kinds of data.
''''
#Numeric Types

# Integers
age = 25
binary = 0b1010      # Binary (10 in decimal)
hexadecimal = 0xFF   # Hexadecimal (255 in decimal)

# Floating-point numbers
height = 5.9
scientific = 1.2e-4  # 0.00012

# Complex numbers
complex_num = 3 + 4j
print(complex_num.real)  # 3.0
print(complex_num.imag)  # 4.0

# Boolean
is_student = True
is_graduated = False
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("Hi"))   # True

#Sequence Types
#python
# String (immutable)
text = "Python Programming"

# List (mutable)
fruits = ["apple", "banana", "orange"]
fruits.append("grape")

# Tuple (immutable)
coordinates = (10, 20)

# Range
numbers = range(5)        # 0,1,2,3,4
even_numbers = range(2, 10, 2)  # 2,4,6,8
Mapping Type
python
# Dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Set Types
# python
# Set (unordered, unique)
unique_numbers = {1, 2, 3, 3, 4}  # {1,2,3,4}

# Frozen set (immutable)
frozen = frozenset([1, 2, 3])
None Type
python
result = None  # Represents absence of value
