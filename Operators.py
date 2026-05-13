'''
4. Operators
Explanation: Operators perform operations on variables and values.
'''
# Arithmetic Operators
# python
a, b = 10, 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor division: 3
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000

# Augmented assignment
x = 5
x += 3   # x = x + 3
x -= 2   # x = x - 2
x *= 4   # x = x * 4


# Comparison Operators
x, y = 5, 10

print(x == y)   # Equal: False
print(x != y)   # Not equal: True
print(x < y)    # Less than: True
print(x > y)    # Greater than: False
print(x <= y)   # Less than or equal: True
print(x >= y)   # Greater than or equal: False

# Logical Operators
# python
a, b = True, False

print(a and b)   # AND: False
print(a or b)    # OR: True
print(not a)     # NOT: False

# Short-circuit evaluation
def risky_function():
    return True

# Second condition not evaluated if first is False
if False and risky_function():
    print("This won't execute")
  
# Bitwise Operators
# python
x, y = 5, 3  # 5: 0101, 3: 0011

print(x & y)   # AND: 1 (0001)
print(x | y)   # OR: 7 (0111)
print(x ^ y)   # XOR: 6 (0110)
print(~x)      # NOT: -6 (two's complement)
print(x << 1)  # Left shift: 10 (1010)
print(x >> 1)  # Right shift: 2 (0010)
Membership Operators
python
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)      # True
print("grape" not in fruits)  # True

# For strings
text = "Hello, World!"
print("World" in text)  # True

# Identity Operators
# python

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)      # True (same object)
print(a is b)      # False (different objects with same content)
print(a == b)      # True (same content)
print(a is not b)  # True
