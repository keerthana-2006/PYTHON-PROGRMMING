#Lambda Functions
# Lambda (anonymous function)
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 7))  # 10

# Lambda with condition
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))  # 20

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
